# --- MOTOR HTML5 / JS CANVAS — MMORPG 2D CON SPRITES Y ENTIDADES DETALLADAS ---

def generar_canvas_html(es_caza, zona_actual, mobs_zona, jefes_zona):
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
            body {{ background-color: #0b1017; color: #fff; margin: 0; padding: 0; overflow: hidden; font-family: 'Courier New', monospace; }}
            #gameContainer {{ position: relative; width: 100vw; height: 92vh; }}
            canvas {{ background: #1b2811; display: block; width: 100%; height: 100%; image-rendering: pixelated; cursor: crosshair; }}
            
            .mmorpg-top-hud {{
                position: absolute; top: 12px; left: 15px; right: 15px;
                display: flex; justify-content: space-between; align-items: center;
                pointer-events: none; z-index: 10;
            }}
            .player-frame {{
                background: rgba(15, 23, 42, 0.92); border: 2px solid #b45309; padding: 10px 18px;
                border-radius: 8px; box-shadow: 0 6px 16px rgba(0,0,0,0.8); display: flex; flex-direction: column; gap: 5px;
            }}
            .hp-bar-bg {{ width: 200px; height: 14px; background: #450a0a; border: 1px solid #7f1d1d; border-radius: 4px; overflow: hidden; }}
            .hp-bar-fill {{ width: 100%; height: 100%; background: #dc2626; transition: width 0.2s ease-in-out; }}
            
            .minimap-frame {{
                width: 140px; height: 140px; background: rgba(15, 23, 42, 0.92);
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
                transition: transform 0.1s;
            }}
            .action-slot:hover {{ transform: scale(1.08); border-color: #f59e0b; }}
            .action-slot span {{ position: absolute; bottom: 2px; right: 5px; font-size: 10px; color: #94a3b8; }}
        </style>
    </head>
    <body>
        <div id="gameContainer">
            <div class="mmorpg-top-hud">
                <div class="player-frame">
                    <div style="font-size: 14px; font-weight: bold; color: #facc15;">⭐ Héroe Nv.1 ({zona_actual})</div>
                    <div class="hp-bar-bg"><div id="hpFill" class="hp-bar-fill"></div></div>
                    <div id="hpText" style="font-size: 11px; color: #cbd5e1;">HP: 100 / 100</div>
                </div>
                
                <div class="minimap-frame">
                    <canvas id="miniCanvas" width="130" height="130"></canvas>
                </div>
            </div>

            <canvas id="gameCanvas"></canvas>

            <div class="mmorpg-action-bar">
                <div class="action-slot" title="Habilidad 1">🔥<span>1</span></div>
                <div class="action-slot" title="Habilidad 2">⚔️<span>2</span></div>
                <div class="action-slot" title="Habilidad 3">🛡️<span>3</span></div>
                <div class="action-slot" title="Poción de Vida">🧪<span>4</span></div>
                <div class="action-slot" title="Poción de Maná">💧<span>5</span></div>
                <div class="action-slot" title="Ataque Básico">🗡️<span>Q</span></div>
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
                x: 2500, y: 2500, size: 24, speed: 5, hp: 100, maxHp: 100, name: "Héroe",
                facing: "down", isMoving: false, animFrame: 0 
            }};
            let keys = {{}};
            let enemies = [];
            
            let structures = [
                {{ x: 2300, y: 2300, w: 240, h: 190, name: "Aurelia Capital", type: "city" }},
                {{ x: 3400, y: 1400, w: 200, h: 200, name: "Castillo de Hojacero", type: "castle" }},
                {{ x: 1300, y: 3100, w: 180, h: 160, name: "Baluarte Enano", type: "fortress" }},
                {{ x: 900, y: 1100, w: 160, h: 150, name: "Puerto Marítimo", type: "port" }}
            ];

            let scenery = [];
            for(let i=0; i<150; i++) {{
                scenery.push({{
                    x: Math.random() * 4800 + 100,
                    y: Math.random() * 4800 + 100,
                    type: Math.random() > 0.35 ? 'tree' : 'rock',
                    size: Math.random() * 25 + 28
                }});
            }}

            let templateMobs = {str(mobs_js_data)};

            for(let i=0; i < 50; i++) {{
                let tmpl = templateMobs.length > 0 ? templateMobs[Math.floor(Math.random() * templateMobs.length)] : {{nombre: "Goblin", hp: 80, ataque_tipo: "Físico", velocidad: 2}};
                enemies.push({{
                    x: Math.random() * 4600 + 200,
                    y: Math.random() * 4600 + 200,
                    size: 20,
                    speed: tmpl.velocidad || 1.8,
                    hp: tmpl.hp,
                    maxHp: tmpl.hp,
                    name: tmpl.nombre,
                    cooldown: 0
                }});
            }}
            
            window.addEventListener("keydown", (e) => keys[e.key] = true);
            window.addEventListener("keyup", (e) => keys[e.key] = false);
            
            function update() {{
                let dx = 0, dy = 0;
                if (keys["ArrowUp"] || keys["w"] || keys["W"]) {{ dy -= player.speed; player.facing = "up"; }}
                if (keys["ArrowDown"] || keys["s"] || keys["S"]) {{ dy += player.speed; player.facing = "down"; }}
                if (keys["ArrowLeft"] || keys["a"] || keys["A"]) {{ dx -= player.speed; player.facing = "left"; }}
                if (keys["ArrowRight"] || keys["d"] || keys["D"]) {{ dx += player.speed; player.facing = "right"; }}
                
                player.isMoving = (dx !== 0 || dy !== 0);
                if (player.isMoving) player.animFrame += 0.2;

                player.x += dx;
                player.y += dy;
                player.x = Math.max(60, Math.min(4940, player.x));
                player.y = Math.max(60, Math.min(4940, player.y));

                enemies.forEach(en => {{
                    let edx = player.x - en.x;
                    let edy = player.y - en.y;
                    let dist = Math.sqrt(edx*edx + edy*edy);
                    if (dist < 420 && dist > 22) {{
                        en.x += (edx / dist) * en.speed;
                        en.y += (edy / dist) * en.speed;
                    }}
                    en.cooldown++;
                    if (dist < 35 && en.cooldown > 50) {{
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
                
                // Sombra en el suelo
                ctx.fillStyle = "rgba(0,0,0,0.4)";
                ctx.beginPath();
                ctx.ellipse(0, 16, 14, 7, 0, 0, Math.PI * 2);
                ctx.fill();

                // Capa / Armadura torso
                ctx.fillStyle = "#1e3a8a"; // túnica azul oscura
                ctx.fillRect(-10, -10, 20, 22);

                // Cabeza / Casco
                ctx.fillStyle = "#fde047"; // casco dorado
                ctx.beginPath();
                ctx.arc(0, -12, 10, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = "#ca8a04";
                ctx.lineWidth = 2;
                ctx.stroke();

                // Hombreras
                ctx.fillStyle = "#d97706";
                ctx.fillRect(-13, -12, 6, 8);
                ctx.fillRect(7, -12, 6, 8);

                // Espada equipada en mano
                ctx.fillStyle = "#e2e8f0";
                ctx.fillRect(12, -6, 4, 18);
                ctx.fillStyle = "#b45309";
                ctx.fillRect(10, 8, 8, 3);

                ctx.restore();
            }}

            function drawMonsterSprite(x, y, name) {{
                ctx.save();
                ctx.translate(x, y);

                // Sombra
                ctx.fillStyle = "rgba(0,0,0,0.4)";
                ctx.beginPath();
                ctx.ellipse(0, 14, 12, 6, 0, 0, Math.PI * 2);
                ctx.fill();

                // Cuerpo del monstruo (Goblin / Bestia)
                ctx.fillStyle = "#7f1d1d"; // rojo oscuro orco/bestia
                ctx.beginPath();
                ctx.roundRect(-12, -12, 24, 24, [6]);
                ctx.fill();
                ctx.strokeStyle = "#b91c1c";
                ctx.lineWidth = 2;
                ctx.stroke();

                // Ojos brillantes amenazantes
                ctx.fillStyle = "#facc15";
                ctx.fillRect(-6, -6, 4, 4);
                ctx.fillRect(2, -6, 4, 4);

                ctx.restore();
            }}

            function drawPixelSprite(x, y, type, size) {{
                ctx.save();
                ctx.translate(x, y);
                if (type === 'tree') {{
                    ctx.fillStyle = "rgba(0,0,0,0.3)";
                    ctx.beginPath();
                    ctx.ellipse(0, size*0.4, size*0.5, size*0.2, 0, 0, Math.PI*2);
                    ctx.fill();

                    ctx.fillStyle = "#78350f";
                    ctx.fillRect(-6, -size*0.2, 12, size*0.7);
                    
                    ctx.fillStyle = "#14532d";
                    ctx.beginPath();
                    ctx.arc(0, -size*0.4, size*0.75, 0, Math.PI*2);
                    ctx.fill();
                    ctx.fillStyle = "#16a34a";
                    ctx.beginPath();
                    ctx.arc(0, -size*0.6, size*0.5, 0, Math.PI*2);
                    ctx.fill();
                }} else if (type === 'rock') {{
                    ctx.fillStyle = "rgba(0,0,0,0.3)";
                    ctx.beginPath();
                    ctx.ellipse(0, size*0.3, size*0.5, size*0.2, 0, 0, Math.PI*2);
                    ctx.fill();

                    ctx.fillStyle = "#475569";
                    ctx.beginPath();
                    ctx.roundRect(-size*0.5, -size*0.4, size, size*0.7, [8]);
                    ctx.fill();
                    ctx.fillStyle = "#94a3b8";
                    ctx.fillRect(-size*0.2, -size*0.2, size*0.3, size*0.3);
                }}
                ctx.restore();
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.save();
                
                let camX = canvas.width / 2 - player.x;
                let camY = canvas.height / 2 - player.y;
                ctx.translate(camX, camY);
                
                // Terreno estilo césped MMORPG 2D
                ctx.fillStyle = "#1b2811";
                ctx.fillRect(0, 0, 5000, 5000);
                
                ctx.strokeStyle = "#141f0c";
                ctx.lineWidth = 2;
                for(let x=0; x<=5000; x+=180) {{
                    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 5000); ctx.stroke();
                }}
                for(let y=0; y<=5000; y+=180) {{
                    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(5000, y); ctx.stroke();
                }}

                // Dibujar Estructuras, Ciudades y Castillos
                structures.forEach(st => {{
                    ctx.fillStyle = "#334155";
                    ctx.fillRect(st.x, st.y, st.w, st.h);
                    ctx.strokeStyle = "#f59e0b";
                    ctx.lineWidth = 4;
                    ctx.strokeRect(st.x, st.y, st.w, st.h);
                    
                    ctx.fillStyle = "#991b1b";
                    ctx.fillRect(st.x - 12, st.y - 25, st.w + 24, 28);
                    
                    ctx.fillStyle = "#ffffff";
                    ctx.font = "bold 16px 'Courier New', monospace";
                    ctx.textAlign = "center";
                    ctx.fillText(st.name, st.x + st.w/2, st.y - 35);
                }});

                // Dibujar Escenario ordenado por Y para efecto profundidad
                scenery.sort((a,b) => a.y - b.y).forEach(sc => {{
                    drawPixelSprite(sc.x, sc.y, sc.type, sc.size);
                }});

                // Dibujar Monstruos / Enemigos con sprites detallados
                enemies.forEach(en => {{
                    drawMonsterSprite(en.x, en.y, en.name);

                    // Barra de vida del enemigo
                    ctx.fillStyle = "#000";
                    ctx.fillRect(en.x - 22, en.y - 28, 44, 7);
                    ctx.fillStyle = "#22c55e";
                    ctx.fillRect(en.x - 21, en.y - 27, 42 * (en.hp / en.maxHp), 5);

                    ctx.fillStyle = "#f87171";
                    ctx.font = "bold 11px sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(en.name + ` [${{en.nivel}}]`, en.x, en.y - 34);
                }});

                // Dibujar Tu Jugador (Héroe con sprite detallado)
                drawPlayerSprite(player.x, player.y);

                ctx.fillStyle = "#facc15";
                ctx.font = "bold 13px 'Courier New', monospace";
                ctx.textAlign = "center";
                ctx.fillText("⭐ " + player.name, player.x, player.y - 28);
                
                ctx.restore();

                // DIBUJAR MINIMAPA CIRCULAR
                miniCtx.clearRect(0, 0, 130, 130);
                miniCtx.fillStyle = "#0f172a";
                miniCtx.fillRect(0, 0, 130, 130);
                
                let mX = (player.x / 5000) * 130;
                let mY = (player.y / 5000) * 130;
                
                miniCtx.fillStyle = "#ef4444";
                enemies.forEach(en => {{
                    let ex = (en.x / 5000) * 130;
                    let ey = (en.y / 5000) * 130;
                    miniCtx.fillRect(ex-1, ey-1, 2, 2);
                }});

                miniCtx.fillStyle = "#facc15";
                miniCtx.beginPath();
                miniCtx.arc(mX, mY, 3.5, 0, Math.PI*2);
                miniCtx.fill();
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