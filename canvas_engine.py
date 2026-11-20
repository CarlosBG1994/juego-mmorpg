# --- MOTOR HTML5 / JS CANVAS — AGUA BLOQUEADA, CASTILLOS INTERACTIVOS Y GRÁFICOS PULIDOS ---

def generar_canvas_html(zona_actual, montura_equipada, velocidad_base, estilo_cabello, color_armadura, mobs_zona):
    mobs_js_data = []
    for m in mobs_zona:
        mobs_js_data.append({
            "nombre": m["nombre"], "nivel": m["nivel"], "hp": m["hp"],
            "ataque_tipo": m["ataque"], "velocidad": m.get("velocidad", 1.8)
        })

    colores_armadura_map = {
        "Azul Real (Valoria)": "#2563eb",
        "Rojo Sangre": "#dc2626",
        "Verde Esmeralda": "#16a34a",
        "Dorado Divino": "#eab308",
        "Oscuro Abisal": "#475569"
    }
    color_hex = colores_armadura_map.get(color_armadura, "#2563eb")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ background-color: #020617; color: #fff; margin: 0; padding: 0; overflow: hidden; font-family: 'Segoe UI', Tahoma, sans-serif; user-select: none; }}
            #gameContainer {{ position: relative; width: 100vw; height: 92vh; }}
            canvas {{ background: #0284c7; display: block; width: 100%; height: 100%; cursor: crosshair; }}
            
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
            .hp-bar-fill {{ width: 100%; height: 100%; background: #22c55e; transition: width 0.2s ease-in-out; }}
            
            .minimap-frame {{
                width: 140px; height: 140px; background: rgba(15, 23, 42, 0.95);
                border: 3px solid #d97706; border-radius: 50%; box-shadow: 0 6px 20px rgba(0,0,0,0.85);
                display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;
            }}
            
            .mmorpg-action-bar {{
                position: absolute; bottom: 18px; left: 50%; transform: translateX(-50%);
                background: rgba(15, 23, 42, 0.95); border: 2px solid #78350f; padding: 8px 14px;
                border-radius: 10px; display: flex; gap: 10px; pointer-events: auto; z-index: 10;
            }}
            .action-slot {{
                width: 55px; height: 55px; background: #1e293b; border: 2px solid #475569;
                border-radius: 6px; display: flex; flex-direction: column; align-items: center; justify-content: center;
                font-size: 14px; font-weight: bold; color: #facc15; position: relative;
            }}
            .action-slot span {{ font-size: 9px; color: #94a3b8; position: absolute; bottom: 2px; right: 5px; }}
            
            .combat-hint {{
                position: absolute; bottom: 92px; left: 50%; transform: translateX(-50%);
                background: rgba(0,0,0,0.85); border: 1px solid #f59e0b; color: #facc15;
                padding: 6px 18px; border-radius: 6px; font-size: 13px; font-weight: bold;
                pointer-events: none; z-index: 50; text-align: center;
            }}
        </style>
    </head>
    <body>
        <div id="gameContainer">
            <div class="mmorpg-top-hud">
                <div class="player-frame">
                    <div style="font-size: 14px; font-weight: bold; color: #facc15;">⭐ Tu Héroe ({zona_actual})</div>
                    <div style="font-size: 12px; color: #38bdf8;">🐴 Montura: {montura_equipada}</div>
                    <div class="hp-bar-bg"><div id="hpFill" class="hp-bar-fill"></div></div>
                    <div id="hpText" style="font-size: 11px; color: #cbd5e1;">HP: 100 / 100</div>
                </div>
                
                <div class="minimap-frame">
                    <canvas id="miniCanvas" width="130" height="130"></canvas>
                </div>
            </div>

            <div id="interactionHint" class="combat-hint">
                ⚔️ <b>WASD</b> Mover | <b>1-4/Q</b> Habilidades | <span id="portalMsg" style="color:#38bdf8;">Acércate a un Castillo para Entrar (Pulsa E)</span>
            </div>

            <canvas id="gameCanvas"></canvas>

            <div class="mmorpg-action-bar">
                <div class="action-slot">⚔️<span id="cd1">1</span></div>
                <div class="action-slot">🔥<span id="cd2">2</span></div>
                <div class="action-slot">🛡️<span id="cd3">3</span></div>
                <div class="action-slot">⚡<span id="cd4">4</span></div>
                <div class="action-slot">🌀<span id="cdQ">Q</span></div>
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
                x: 3000, y: 3000, radius: 20, speed: {velocidad_base}, hp: 100, maxHp: 100, 
                kills: 0, shieldActive: false, shieldTimer: 0, insideCastle: false, castleName: "",
                cooldowns: {{ '1': 0, '2': 0, '3': 0, '4': 0, 'q': 0 }},
                effectAnim: null, effectProgress: 0
            }};
            
            let keys = {{}};
            let enemies = [];
            
            // Castillos y ciudades con puertas interactivas
            let structures = [
                {{ x: 2400, y: 2400, w: 380, h: 320, name: "Aurelia Capital", type: "city", doorX: 2590, doorY: 2720 }},
                {{ x: 4200, y: 1400, w: 320, h: 320, name: "Castillo de Hojacero", type: "castle", doorX: 4360, doorY: 1720 }},
                {{ x: 1200, y: 3800, w: 280, h: 280, name: "Baluarte Subterráneo", type: "dungeon", doorX: 1340, doorY: 4080 }}
            ];

            let scenery = [];
            for(let i=0; i<100; i++) {{
                scenery.push({{
                    x: Math.random() * 5200 + 400, y: Math.random() * 5200 + 400,
                    type: Math.random() > 0.5 ? 'tree' : 'rock', radius: 24
                }});
            }}

            let templateMobs = {str(mobs_js_data)};
            for(let i=0; i < 35; i++) {{
                let tmpl = templateMobs[Math.floor(Math.random() * templateMobs.length)];
                enemies.push({{
                    x: Math.random() * 5000 + 500, y: Math.random() * 5000 + 500,
                    radius: 18, speed: tmpl.velocidad || 1.8, hp: tmpl.hp, maxHp: tmpl.hp,
                    name: tmpl.nombre, nivel: tmpl.nivel, cooldown: 0
                }});
            }}
            
            window.addEventListener("keydown", (e) => {{
                let k = e.key.toLowerCase();
                keys[e.key] = true;
                if (['1', '2', '3', '4', 'q'].includes(k)) {{
                    handleSkill(k);
                }}
                if (k === 'e') {{
                    checkCastleInteraction();
                }}
            }});
            window.addEventListener("keyup", (e) => keys[e.key] = false);

            function checkCastleInteraction() {{
                if (player.insideCastle) {{
                    player.insideCastle = false;
                    document.getElementById("portalMsg").innerText = "Has salido al mundo exterior.";
                    return;
                }}
                for (let st of structures) {{
                    let distDoor = Math.hypot(player.x - st.doorX, player.y - st.doorY);
                    if (distDoor < 60) {{
                        player.insideCastle = true;
                        player.castleName = st.name;
                        document.getElementById("portalMsg").innerText = `🏰 Estás dentro de ${{st.name}}. Pulsa E para salir.`;
                        break;
                    }}
                }}
            }}

            function handleSkill(key) {{
                if (player.cooldowns[key] > 0) return;
                if (key === '1') {{
                    player.cooldowns['1'] = 25;
                    player.effectAnim = 'slash'; player.effectProgress = 20;
                    damageEnemiesInRadius(75, 45);
                }} else if (key === '2') {{
                    player.cooldowns['2'] = 50;
                    player.effectAnim = 'fire'; player.effectProgress = 30;
                    damageEnemiesInRadius(120, 80);
                }} else if (key === '3') {{
                    player.cooldowns['3'] = 120;
                    player.shieldActive = true;
                    player.shieldTimer = 90;
                }} else if (key === '4' || key === 'q') {{
                    player.cooldowns['4'] = 180;
                    player.cooldowns['q'] = 180;
                    player.effectAnim = 'pulse'; player.effectProgress = 40;
                    damageEnemiesInRadius(180, 120);
                }}
            }}

            function damageEnemiesInRadius(radius, damage) {{
                for (let i = enemies.length - 1; i >= 0; i--) {{
                    let en = enemies[i];
                    let dx = en.x - player.x, dy = en.y - player.y;
                    if (Math.hypot(dx, dy) < radius) {{
                        en.hp -= damage;
                        if (en.hp <= 0) {{ enemies.splice(i, 1); player.kills++; }}
                    }}
                }}
            }}

            // Restricción estricta de terreno: El agua (fuera de la isla central de hierba) bloquea el paso
            function checkCollision(nx, ny, radius) {{
                if (nx < 150 || nx > 5850 || ny < 150 || ny > 5850) return true;
                
                // Si está dentro de un castillo, colisiona con sus murallas interiores
                if (player.insideCastle) {{
                    let st = structures.find(s => s.name === player.castleName);
                    if (st && (nx - radius < st.x + 20 || nx + radius > st.x + st.w - 20 || ny - radius < st.y + 40 || ny + radius > st.y + st.h - 20)) {{
                        // Permitir salida por la puerta
                        let distDoor = Math.hypot(nx - st.doorX, ny - st.doorY);
                        if (distDoor > 45) return true;
                    }}
                    return false;
                }}

                // EL AGUA BLOQUEA EL PASO: El mundo principal de tierra va de x: 800 a 5200, y: 800 a 5200. Fuera de ahí es agua profunda inalcanzable.
                let enTierra = (nx > 850 && nx < 5150 && ny > 850 && ny < 5150);
                
                // También colisiona con los edificios y castillos cerrados
                for (let st of structures) {{
                    if (nx + radius > st.x && nx - radius < st.x + st.w && ny + radius > st.y && ny - radius < st.y + st.h) {{
                        // Permitir pasar si está cerca de la puerta
                        let distDoor = Math.hypot(nx - st.doorX, ny - st.doorY);
                        if (distDoor > 45) return true;
                    }}
                }}
                
                for (let sc of scenery) {{
                    let dx = nx - sc.x, dy = ny - sc.y;
                    if (Math.hypot(dx, dy) < radius + sc.radius * 0.6) return true;
                }}

                return !enTierra; // Si sale de la isla de tierra, choca con el agua
            }}
            
            function update() {{
                let dx = 0, dy = 0;
                if (keys["ArrowUp"] || keys["w"] || keys["W"]) dy -= player.speed;
                if (keys["ArrowDown"] || keys["s"] || keys["S"]) dy += player.speed;
                if (keys["ArrowLeft"] || keys["a"] || keys["A"]) dx -= player.speed;
                if (keys["ArrowRight"] || keys["d"] || keys["D"]) dx += player.speed;
                
                if (!checkCollision(player.x + dx, player.y, player.radius)) player.x += dx;
                if (!checkCollision(player.x, player.y + dy, player.radius)) player.y += dy;

                for (let k in player.cooldowns) {{
                    if (player.cooldowns[k] > 0) player.cooldowns[k]--;
                }}
                if (player.shieldActive) {{
                    player.shieldTimer--;
                    if (player.shieldTimer <= 0) player.shieldActive = false;
                }}
                if (player.effectProgress > 0) {{
                    player.effectProgress--;
                    if (player.effectProgress <= 0) player.effectAnim = null;
                }}

                // Movimiento de enemigos (restringidos a tierra firme)
                enemies.forEach(en => {{
                    let edx = player.x - en.x, edy = player.y - en.y;
                    let dist = Math.hypot(edx, edy);
                    if (dist < 350 && dist > 20 && !player.insideCastle) {{
                        let nextX = en.x + (edx / dist) * en.speed;
                        let nextY = en.y + (edy / dist) * en.speed;
                        // Evitar que enemigos entren al agua
                        if (nextX > 900 && nextX < 5100 && nextY > 900 && nextY < 5100) {{
                            en.x = nextX;
                            en.y = nextY;
                        }}
                    }}
                    en.cooldown++;
                    if (dist < 35 && en.cooldown > 45) {{
                        en.cooldown = 0;
                        if (!player.shieldActive) {{
                            player.hp = Math.max(0, player.hp - 10);
                            document.getElementById("hpFill").style.width = (player.hp / player.maxHp * 100) + "%";
                            document.getElementById("hpText").innerText = `HP: ${{player.hp}} / ${{player.maxHp}}`;
                        }}
                    }}
                }});
            }}

            function drawPlayerSprite(x, y) {{
                ctx.save();
                ctx.translate(x, y);
                ctx.fillStyle = "rgba(0,0,0,0.5)";
                ctx.beginPath(); ctx.ellipse(0, 16, 12, 6, 0, 0, Math.PI * 2); ctx.fill();

                if (player.shieldActive) {{
                    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 4;
                    ctx.fillStyle = "rgba(56, 189, 248, 0.2)";
                    ctx.beginPath(); ctx.arc(0, 0, 30, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                }}

                ctx.fillStyle = "{color_hex}";
                ctx.fillRect(-11, -11, 22, 24);
                ctx.strokeStyle = "#facc15"; ctx.lineWidth = 2; ctx.strokeRect(-11, -11, 22, 24);

                ctx.fillStyle = "#fde047";
                ctx.beginPath(); ctx.arc(0, -15, 10, 0, Math.PI * 2); ctx.fill();
                ctx.stroke();

                if (player.effectAnim) {{
                    ctx.strokeStyle = player.effectAnim === 'fire' ? "#ef4444" : "#facc15";
                    ctx.lineWidth = 4;
                    ctx.beginPath(); ctx.arc(0, 0, 45 - (player.effectProgress * 1.1), 0, Math.PI * 2); ctx.stroke();
                }}
                ctx.restore();
            }}

            function drawMonsterSprite(x, y, name) {{
                ctx.save();
                ctx.translate(x, y);
                ctx.fillStyle = "rgba(0,0,0,0.4)";
                ctx.beginPath(); ctx.ellipse(0, 14, 11, 5, 0, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = "#991b1b"; ctx.beginPath(); ctx.roundRect(-14, -14, 28, 28, [6]); ctx.fill();
                ctx.strokeStyle = "#f87171"; ctx.lineWidth = 2; ctx.stroke();
                ctx.fillStyle = "#facc15"; ctx.fillRect(-6, -5, 3, 3); ctx.fillRect(3, -5, 3, 3);
                ctx.restore();
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.save();
                
                let camX = canvas.width / 2 - player.x;
                let camY = canvas.height / 2 - player.y;
                ctx.translate(camX, camY);
                
                if (player.insideCastle) {{
                    // Interiores del castillo detallados
                    ctx.fillStyle = "#1e293b"; ctx.fillRect(player.x - 600, player.y - 600, 1200, 1200);
                    ctx.strokeStyle = "#d97706"; ctx.lineWidth = 8; ctx.strokeRect(player.x - 550, player.y - 550, 1100, 1100);
                    
                    ctx.fillStyle = "#facc15"; ctx.font = "bold 24px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(`🏰 Interior de ${{player.castleName}}`, player.x, player.y - 200);
                    ctx.font = "bold 14px sans-serif";
                    ctx.fillText("Salón del Trono y Comercio Real (Pulsa E para salir)", player.x, player.y - 160);
                    
                    drawPlayerSprite(player.x, player.y);
                    ctx.restore();
                    return;
                }}

                // MUNDO EXTERIOR: Océano de fondo (agua profunda)
                ctx.fillStyle = "#0284c7"; ctx.fillRect(0, 0, 6000, 6000);
                
                // Isla central de tierra firme con césped detallado
                ctx.fillStyle = "#166534"; ctx.fillRect(800, 800, 4400, 4400);
                ctx.fillStyle = "#15803d"; ctx.fillRect(850, 850, 4300, 4300);

                // Dibujar Castillos y Ciudades con sus Puertas
                structures.forEach(st => {{
                    ctx.fillStyle = st.type === 'dungeon' ? "#450a0a" : "#334155";
                    ctx.fillRect(st.x, st.y, st.w, st.h);
                    ctx.strokeStyle = st.type === 'dungeon' ? "#dc2626" : "#f59e0b";
                    ctx.lineWidth = 5; ctx.strokeRect(st.x, st.y, st.w, st.h);
                    
                    // Puerta de entrada interactiva
                    ctx.fillStyle = "#78350f"; ctx.fillRect(st.doorX - 20, st.doorY - 15, 40, 30);
                    ctx.strokeStyle = "#facc15"; ctx.lineWidth = 2; ctx.strokeRect(st.doorX - 20, st.doorY - 15, 40, 30);

                    ctx.fillStyle = "#991b1b"; ctx.fillRect(st.x - 10, st.y - 30, st.w + 20, 30);
                    ctx.fillStyle = "#ffffff"; ctx.font = "bold 15px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(st.name + " [Pulsa E en la Puerta]", st.x + st.w/2, st.y - 10);
                }});

                scenery.forEach(sc => {{
                    if (sc.type === 'tree') {{
                        ctx.fillStyle = "#14532d"; ctx.beginPath(); ctx.arc(sc.x, sc.y - 10, sc.radius, 0, Math.PI*2); ctx.fill();
                    }} else {{
                        ctx.fillStyle = "#475569"; ctx.beginPath(); ctx.roundRect(sc.x - sc.radius, sc.y - sc.radius*0.7, sc.radius*2, sc.radius*1.4, [6]); ctx.fill();
                    }}
                }});

                enemies.forEach(en => {{
                    drawMonsterSprite(en.x, en.y, en.name);
                    ctx.fillStyle = "#000"; ctx.fillRect(en.x - 20, en.y - 28, 40, 6);
                    ctx.fillStyle = "#22c55e"; ctx.fillRect(en.x - 19, en.y - 27, 38 * (en.hp / en.maxHp), 4);
                    ctx.fillStyle = "#f87171"; ctx.font = "bold 11px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(en.name + ` [${{en.nivel}}]`, en.x, en.y - 34);
                }});

                drawPlayerSprite(player.x, player.y);
                ctx.fillStyle = "#facc15"; ctx.font = "bold 13px sans-serif"; ctx.textAlign = "center";
                ctx.fillText("⭐ Tu Héroe (Kills: " + player.kills + ")", player.x, player.y - 30);
                
                ctx.restore();

                miniCtx.clearRect(0, 0, 130, 130);
                miniCtx.fillStyle = "#0f172a"; miniCtx.fillRect(0, 0, 130, 130);
                let mX = (player.x / 6000) * 130, mY = (player.y / 6000) * 130;
                miniCtx.fillStyle = "#facc15"; miniCtx.beginPath(); miniCtx.arc(mX, mY, 3.5, 0, Math.PI*2); miniCtx.fill();
            }}
            
            function loop() {{ update(); draw(); requestAnimationFrame(loop); }}
            loop();
        </script>
    </body>
    </html>
    """