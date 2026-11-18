# --- MOTOR HTML5 / JS CANVAS — MMORPG 2D DEFINITIVO ---

def generar_canvas_html(zona_actual, montura_equipada, velocidad_base, mobs_zona):
    mobs_js_data = []
    for m in mobs_zona:
        mobs_js_data.append({
            "nombre": m["nombre"],
            "nivel": m["nivel"],
            "hp": m["hp"],
            "ataque_tipo": m["ataque"],
            "velocidad": m.get("velocidad", 1.8)
        })

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ background-color: #020617; color: #fff; margin: 0; padding: 0; overflow: hidden; font-family: 'Segoe UI', Tahoma, sans-serif; user-select: none; }}
            #gameContainer {{ position: relative; width: 100vw; height: 92vh; }}
            canvas {{ background: #0369a1; display: block; width: 100%; height: 100%; cursor: crosshair; }}
            
            .mmorpg-top-hud {{
                position: absolute; top: 12px; left: 15px; right: 15px;
                display: flex; justify-content: space-between; align-items: center;
                pointer-events: none; z-index: 10;
            }}
            .player-frame {{
                background: rgba(15, 23, 42, 0.95); border: 2px solid #b45309; padding: 10px 18px;
                border-radius: 8px; box-shadow: 0 6px 16px rgba(0,0,0,0.8); display: flex; flex-direction: column; gap: 5px;
                pointer-events: auto;
            }}
            .hp-bar-bg {{ width: 200px; height: 14px; background: #450a0a; border: 1px solid #7f1d1d; border-radius: 4px; overflow: hidden; }}
            .hp-bar-fill {{ width: 100%; height: 100%; background: #dc2626; transition: width 0.2s ease-in-out; }}
            
            .minimap-frame {{
                width: 140px; height: 140px; background: rgba(15, 23, 42, 0.95);
                border: 3px solid #d97706; border-radius: 50%; box-shadow: 0 6px 20px rgba(0,0,0,0.85);
                display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;
            }}
            
            .mmorpg-action-bar {{
                position: absolute; bottom: 18px; left: 50%; transform: translateX(-50%);
                background: rgba(15, 23, 42, 0.95); border: 2px solid #78350f; padding: 8px 14px;
                border-radius: 10px; display: flex; gap: 10px; pointer-events: auto; z-index: 10;
                box-shadow: 0 10px 30px rgba(0,0,0,0.9);
            }}
            .action-slot {{
                width: 50px; height: 50px; background: #1e293b; border: 2px solid #475569;
                border-radius: 6px; display: flex; align-items: center; justify-content: center;
                font-size: 15px; font-weight: bold; color: #facc15; cursor: pointer; position: relative;
            }}
            .action-slot span {{ position: absolute; bottom: 2px; right: 5px; font-size: 10px; color: #94a3b8; }}

            .combat-hint {{
                position: absolute; bottom: 90px; left: 50%; transform: translateX(-50%);
                background: rgba(0,0,0,0.85); border: 1px solid #f59e0b; color: #facc15;
                padding: 6px 18px; border-radius: 6px; font-size: 13px; font-weight: bold;
                pointer-events: none; z-index: 50; box-shadow: 0 4px 12px rgba(0,0,0,0.6);
            }}
        </style>
    </head>
    <body>
        <div id="gameContainer">
            <div class="mmorpg-top-hud">
                <div class="player-frame">
                    <div style="font-size: 14px; font-weight: bold; color: #facc15;">⭐ Héroe Nv.1 ({zona_actual})</div>
                    <div style="font-size: 12px; color: #38bdf8;">🐴 Montura: {montura_equipada}</div>
                    <div class="hp-bar-bg"><div id="hpFill" class="hp-bar-fill"></div></div>
                    <div id="hpText" style="font-size: 11px; color: #cbd5e1;">HP: 100 / 100</div>
                </div>
                
                <div class="minimap-frame">
                    <canvas id="miniCanvas" width="130" height="130"></canvas>
                </div>
            </div>

            <div class="combat-hint">⚔️ <b>W,A,S,D</b> para moverte | <b>ESPACIO / Q</b> para Atacar | Colisiones estrictas activas.</div>

            <canvas id="gameCanvas"></canvas>

            <div class="mmorpg-action-bar">
                <div class="action-slot" title="Ataque">⚔️<span>1</span></div>
                <div class="action-slot" title="Fuego">🔥<span>2</span></div>
                <div class="action-slot" title="Escudo">🛡️<span>3</span></div>
                <div class="action-slot" title="Poción">🧪<span>4</span></div>
                <div class="action-slot" title="Maná">💧<span>5</span></div>
                <div class="action-slot" title="Especial">🗡️<span>Q</span></div>
            </div>
        </div>
        
        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            const miniCanvas = document.getElementById("miniCanvas");
            const miniCtx = miniCanvas.getContext("2d");
            
            function resizeCanvas() {{
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight * 0.92;
            }}
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();

            let player = {{ 
                x: 3000, y: 3000, radius: 18, speed: {velocidad_base}, hp: 100, maxHp: 100, name: "Héroe", kills: 0, isAttacking: false, attackAnim: 0 
            }};
            let keys = {{}};
            let enemies = [];
            
            let structures = [
                {{ x: 2500, y: 2500, w: 350, h: 300, name: "Aurelia Capital", type: "city" }},
                {{ x: 4000, y: 1500, w: 280, h: 280, name: "Castillo de Hojacero", type: "castle" }},
                {{ x: 1400, y: 3500, w: 250, h: 250, name: "Mazmorra Subterránea [Nivel 50]", type: "dungeon" }},
                {{ x: 1000, y: 1200, w: 300, h: 250, name: "Puerto Comercial del Sur", type: "port" }}
            ];

            let scenery = [];
            for(let i=0; i<150; i++) {{
                scenery.push({{
                    x: Math.random() * 5400 + 300,
                    y: Math.random() * 5400 + 300,
                    type: Math.random() > 0.4 ? 'tree' : 'rock',
                    radius: 24
                }});
            }}

            let templateMobs = {str(mobs_js_data)};
            for(let i=0; i < 50; i++) {{
                let tmpl = templateMobs[Math.floor(Math.random() * templateMobs.length)];
                enemies.push({{
                    x: Math.random() * 5200 + 400,
                    y: Math.random() * 5200 + 400,
                    radius: 18,
                    speed: tmpl.velocidad || 1.8,
                    hp: tmpl.hp,
                    maxHp: tmpl.hp,
                    name: tmpl.nombre,
                    nivel: tmpl.nivel,
                    cooldown: 0
                }});
            }}
            
            window.addEventListener("keydown", (e) => {{
                keys[e.key] = true;
                if (e.key === " " || e.key === "q" || e.key === "Q") performAttack();
            }});
            window.addEventListener("keyup", (e) => keys[e.key] = false);

            function performAttack() {{
                player.isAttacking = true;
                player.attackAnim = 10;
                enemies.forEach((en, index) => {{
                    let dx = en.x - player.x, dy = en.y - player.y;
                    if (Math.sqrt(dx*dx + dy*dy) < 65) {{
                        en.hp -= 50;
                        if (en.hp <= 0) {{
                            enemies.splice(index, 1);
                            player.kills++;
                        }}
                    }}
                }});
            }}

            function checkCollision(nx, ny, radius) {{
                if (nx < 100 || nx > 5900 || ny < 100 || ny > 5900) return true;
                for (let st of structures) {{
                    if (nx + radius > st.x && nx - radius < st.x + st.w &&
                        ny + radius > st.y && ny - radius < st.y + st.h) {{
                        return true;
                    }}
                }}
                for (let sc of scenery) {{
                    let dx = nx - sc.x, dy = ny - sc.y;
                    if (Math.sqrt(dx*dx + dy*dy) < radius + sc.radius * 0.75) return true;
                }}
                return false;
            }}
            
            function update() {{
                let dx = 0, dy = 0;
                if (keys["ArrowUp"] || keys["w"] || keys["W"]) dy -= player.speed;
                if (keys["ArrowDown"] || keys["s"] || keys["S"]) dy += player.speed;
                if (keys["ArrowLeft"] || keys["a"] || keys["A"]) dx -= player.speed;
                if (keys["ArrowRight"] || keys["d"] || keys["D"]) dx += player.speed;
                
                if (!checkCollision(player.x + dx, player.y, player.radius)) player.x += dx;
                if (!checkCollision(player.x, player.y + dy, player.radius)) player.y += dy;

                if (player.attackAnim > 0) player.attackAnim--;
                else player.isAttacking = false;

                enemies.forEach(en => {{
                    let edx = player.x - en.x, edy = player.y - en.y;
                    let dist = Math.sqrt(edx*edx + edy*edy);
                    if (dist < 380 && dist > 20) {{
                        en.x += (edx / dist) * en.speed;
                        en.y += (edy / dist) * en.speed;
                    }}
                    en.cooldown++;
                    if (dist < 32 && en.cooldown > 50) {{
                        en.cooldown = 0;
                        player.hp = Math.max(0, player.hp - 10);
                        document.getElementById("hpFill").style.width = (player.hp / player.maxHp * 100) + "%";
                        document.getElementById("hpText").innerText = `HP: ${{player.hp}} / ${{player.maxHp}}`;
                    }}
                }});
            }}

            function drawPlayerSprite(x, y) {{
                ctx.save();
                ctx.translate(x, y);
                ctx.fillStyle = "rgba(0,0,0,0.5)";
                ctx.beginPath(); ctx.ellipse(0, 14, 12, 6, 0, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = "#1e3a8a"; ctx.fillRect(-9, -9, 18, 20);
                ctx.fillStyle = "#fde047"; ctx.beginPath(); ctx.arc(0, -10, 9, 0, Math.PI * 2); ctx.fill();
                ctx.strokeStyle = "#ca8a04"; ctx.lineWidth = 2; ctx.stroke();

                if (player.isAttacking) {{
                    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 4;
                    ctx.beginPath(); ctx.arc(0, 0, 35, 0, Math.PI * 2); ctx.stroke();
                }}
                ctx.fillStyle = "#e2e8f0"; ctx.fillRect(10, -5, 4, 16);
                ctx.restore();
            }}

            function drawMonsterSprite(x, y, name) {{
                ctx.save();
                ctx.translate(x, y);
                ctx.fillStyle = "rgba(0,0,0,0.5)";
                ctx.beginPath(); ctx.ellipse(0, 12, 10, 5, 0, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = "#7f1d1d"; ctx.beginPath(); ctx.roundRect(-12, -12, 24, 24, [6]); ctx.fill();
                ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2; ctx.stroke();
                ctx.fillStyle = "#facc15"; ctx.fillRect(-5, -5, 3, 3); ctx.fillRect(2, -5, 3, 3);
                ctx.restore();
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.save();
                
                let camX = canvas.width / 2 - player.x;
                let camY = canvas.height / 2 - player.y;
                ctx.translate(camX, camY);
                
                ctx.fillStyle = "#0284c7"; ctx.fillRect(0, 0, 6000, 6000);
                ctx.fillStyle = "#1a2e12"; ctx.fillRect(800, 800, 4400, 4400);

                structures.forEach(st => {{
                    ctx.fillStyle = st.type === 'dungeon' ? "#450a0a" : "#334155";
                    ctx.fillRect(st.x, st.y, st.w, st.h);
                    ctx.strokeStyle = st.type === 'dungeon' ? "#dc2626" : "#f59e0b";
                    ctx.lineWidth = 4;
                    ctx.strokeRect(st.x, st.y, st.w, st.h);
                    
                    ctx.fillStyle = "#991b1b"; ctx.fillRect(st.x - 10, st.y - 25, st.w + 20, 26);
                    ctx.fillStyle = "#ffffff"; ctx.font = "bold 14px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(st.name, st.x + st.w/2, st.y - 35);
                }});

                scenery.forEach(sc => {{
                    if (sc.type === 'tree') {{
                        ctx.fillStyle = "#14532d"; ctx.beginPath(); ctx.arc(sc.x, sc.y - 10, sc.radius, 0, Math.PI*2); ctx.fill();
                    }} else {{
                        ctx.fillStyle = "#475569"; ctx.beginPath(); ctx.roundRect(sc.x - sc.radius, sc.y - sc.radius*0.7, sc.radius*2, sc.radius*1.4, [8]); ctx.fill();
                    }}
                }});

                enemies.forEach(en => {{
                    drawMonsterSprite(en.x, en.y, en.name);
                    ctx.fillStyle = "#000"; ctx.fillRect(en.x - 20, en.y - 26, 40, 6);
                    ctx.fillStyle = "#22c55e"; ctx.fillRect(en.x - 19, en.y - 25, 38 * (en.hp / en.maxHp), 4);
                    ctx.fillStyle = "#f87171"; ctx.font = "bold 11px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(en.name + ` [${{en.nivel}}]`, en.x, en.y - 32);
                }});

                drawPlayerSprite(player.x, player.y);
                ctx.fillStyle = "#facc15"; ctx.font = "bold 13px sans-serif"; ctx.textAlign = "center";
                ctx.fillText("⭐ " + player.name + ` (Kills: ${{player.kills}})`, player.x, player.y - 26);
                
                ctx.restore();

                miniCtx.clearRect(0, 0, 130, 130);
                miniCtx.fillStyle = "#0f172a"; miniCtx.fillRect(0, 0, 130, 130);
                let mX = (player.x / 6000) * 130, mY = (player.y / 6000) * 130;
                miniCtx.fillStyle = "#facc15"; miniCtx.beginPath(); miniCtx.arc(mX, mY, 3.5, 0, Math.PI*2); miniCtx.fill();
            }}
            
            function loop() {{
                update();
                draw();
                requestAnimationFrame(loop);
            }}
            
            loop();
        </script>
    </body>
    </html>
    """