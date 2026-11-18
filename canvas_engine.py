# --- MOTOR HTML5 / JS CANVAS — MMORPG 2D ESTILO PIXEL ART / TILESET ---

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
            canvas {{ background: #223414; display: block; width: 100%; height: 100%; image-rendering: pixelated; cursor: crosshair; }}
            
            /* HUD Superior estilo MMORPG */
            .mmorpg-top-hud {{
                position: absolute; top: 10px; left: 15px; right: 15px;
                display: flex; justify-content: space-between; align-items: center;
                pointer-events: none;
            }}
            .player-frame {{
                background: rgba(15, 23, 42, 0.85); border: 2px solid #854d0e; padding: 8px 15px;
                border-radius: 6px; box-shadow: 0 4px 10px rgba(0,0,0,0.6); display: flex; flex-direction: column; gap: 4px;
            }}
            .hp-bar-bg {{ width: 160px; height: 14px; background: #450a0a; border: 1px solid #7f1d1d; border-radius: 3px; overflow: hidden; }}
            .hp-bar-fill {{ width: 100%; height: 100%; background: #dc2626; transition: width 0.2s; }}
            
            .minimap-frame {{
                width: 130px; height: 130px; background: rgba(15, 23, 42, 0.9);
                border: 3px solid #b45309; border-radius: 50%; box-shadow: 0 4px 15px rgba(0,0,0,0.8);
                display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;
            }}
            
            /* Barra de Acciones Rápida Inferior */
            .mmorpg-action-bar {{
                position: absolute; bottom: 15px; left: 50%; transform: translateX(-50%);
                background: rgba(15, 23, 42, 0.9); border: 2px solid #78350f; padding: 8px 12px;
                border-radius: 8px; display: flex; gap: 8px; pointer-events: auto;
                box-shadow: 0 8px 20px rgba(0,0,0,0.8);
            }}
            .action-slot {{
                width: 45px; height: 45px; background: #1e293b; border: 2px solid #475569;
                border-radius: 4px; display: flex; align-items: center; justify-content: center;
                font-size: 12px; font-weight: bold; color: #facc15; cursor: pointer; position: relative;
            }}
            .action-slot span {{ position: absolute; bottom: 2px; right: 4px; font-size: 9px; color: #94a3b8; }}
        </style>
    </head>
    <body>
        <div id="gameContainer">
            <!-- HUD SUPERIOR -->
            <div class="mmorpg-top-hud">
                <div class="player-frame">
                    <div style="font-size: 13px; font-weight: bold; color: #facc15;">⭐ Héroe Nv.1 ({zona_actual})</div>
                    <div class="hp-bar-bg"><div id="hpFill" class="hp-bar-fill"></div></div>
                    <div id="hpText" style="font-size: 10px; color: #cbd5e1;">HP: 100 / 100</div>
                </div>
                
                <div class="minimap-frame">
                    <canvas id="miniCanvas" width="120" height="120"></canvas>
                </div>
            </div>

            <canvas id="gameCanvas"></canvas>

            <!-- BARRA INFERIOR DE HABILIDADES TIPO MMORPG -->
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

            let player = {{ x: 2500, y: 2500, size: 28, speed: 4.5, hp: 100, maxHp: 100, name: "Héroe" }};
            let keys = {{}};
            let enemies = [];
            
            // Ciudades, Castillos y Estructuras en Tilemap 2D
            let structures = [
                {{ x: 2300, y: 2300, w: 200, h: 160, name: "Aurelia Capital", type: "city" }},
                {{ x: 3400, y: 1500, w: 180, h: 180, name: "Castillo de Hojacero", type: "castle" }},
                {{ x: 1400, y: 3200, w: 160, h: 140, name: "Baluarte Enano", type: "fortress" }},
                {{ x: 1000, y: 1200, w: 140, h: 140, name: "Puerto Marítimo", type: "port" }}
            ];

            // Generación de entorno 2D (Árboles, rocas, hogueras)
            let scenery = [];
            for(let i=0; i<120; i++) {{
                scenery.push({{
                    x: Math.random() * 4800 + 100,
                    y: Math.random() * 4800 + 100,
                    type: Math.random() > 0.3 ? 'tree' : 'rock',
                    size: Math.random() * 20 + 25
                }});
            }}

            let templateMobs = {str(mobs_js_data)};
            let derrotadosCount = 0;

            for(let i=0; i < 50; i++) {{
                let tmpl = templateMobs.length > 0 ? templateMobs[Math.floor(Math.random() * templateMobs.length)] : {{nombre: "Goblin", hp: 80, ataque_tipo: "Físico", velocidad: 2}};
                enemies.push({{
                    x: Math.random() * 4600 + 200,
                    y: Math.random() * 4600 + 200,
                    size: 22,
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
                if (keys["ArrowUp"] || keys["w"] || keys["W"]) dy -= player.speed;
                if (keys["ArrowDown"] || keys["s"] || keys["S"]) dy += player.speed;
                if (keys["ArrowLeft"] || keys["a"] || keys["A"]) dx -= player.speed;
                if (keys["ArrowRight"] || keys["d"] || keys["D"]) dx += player.speed;
                
                player.x += dx;
                player.y += dy;
                player.x = Math.max(50, Math.min(4950, player.x));
                player.y = Math.max(50, Math.min(4950, player.y));

                // IA Enemiga de persecución
                enemies.forEach(en => {{
                    let edx = player.x - en.x;
                    let edy = player.y - en.y;
                    let dist = Math.sqrt(edx*edx + edy*edy);
                    if (dist < 400 && dist > 20) {{
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

            function drawPixelSprite(x, y, type, size) {{
                ctx.save();
                ctx.translate(x, y);
                if (type === 'tree') {{
                    // Tronco
                    ctx.fillStyle = "#78350f";
                    ctx.fillRect(-6, 0, 12, size);
                    // Copa de pino / árbol frondoso 2D
                    ctx.fillStyle = "#166534";
                    ctx.beginPath();
                    ctx.arc(0, -size*0.4, size*0.8, 0, Math.PI*2);
                    ctx.fill();
                    ctx.fillStyle = "#22c55e";
                    ctx.beginPath();
                    ctx.arc(0, -size*0.6, size*0.5, 0, Math.PI*2);
                    ctx.fill();
                }} else if (type === 'rock') {{
                    ctx.fillStyle = "#64748b";
                    ctx.beginPath();
                    ctx.roundRect(-size*0.5, -size*0.3, size, size*0.7, [6]);
                    ctx.fill();
                    ctx.fillStyle = "#94a3b8";
                    ctx.fillRect(-size*0.2, -size*0.1, size*0.4, size*0.3);
                }}
                ctx.restore();
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.save();
                
                let camX = canvas.width / 2 - player.x;
                let camY = canvas.height / 2 - player.y;
                ctx.translate(camX, camY);
                
                // Terreno estilo césped MMORPG 2D con textura de cuadrícula sutil
                ctx.fillStyle = "#223414";
                ctx.fillRect(0, 0, 5000, 5000);
                
                ctx.strokeStyle = "#1b2a0f";
                ctx.lineWidth = 2;
                for(let x=0; x<=5000; x+=150) {{
                    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 5000); ctx.stroke();
                }}
                for(let y=0; y<=5000; y+=150) {{
                    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(5000, y); ctx.stroke();
                }}

                // Dibujar Estructuras, Ciudades y Castillos 2D
                structures.forEach(st => {{
                    ctx.fillStyle = "#334155";
                    ctx.fillRect(st.x, st.y, st.w, st.h);
                    ctx.strokeStyle = "#f59e0b";
                    ctx.lineWidth = 4;
                    ctx.strokeRect(st.x, st.y, st.w, st.h);
                    
                    // Techo o detalles del castillo
                    ctx.fillStyle = "#b91c1c";
                    ctx.fillRect(st.x - 10, st.y - 20, st.w + 20, 25);
                    
                    ctx.fillStyle = "#ffffff";
                    ctx.font = "bold 14px 'Courier New', monospace";
                    ctx.textAlign = "center";
                    ctx.fillText(st.name, st.x + st.w/2, st.y - 30);
                }});

                // Dibujar Escenario (Árboles y Rocas)
                scenery.forEach(sc => {{
                    drawPixelSprite(sc.x, sc.y, sc.type, sc.size);
                }});

                // Dibujar Monstruos / Enemigos 2D
                enemies.forEach(en => {{
                    ctx.fillStyle = "#991b1b";
                    ctx.beginPath();
                    ctx.arc(en.x, en.y, en.size, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = "#f87171";
                    ctx.stroke();

                    // Mini barra de vida enemigo
                    ctx.fillStyle = "#000";
                    ctx.fillRect(en.x - 18, en.y - en.size - 12, 36, 6);
                    ctx.fillStyle = "#22c55e";
                    ctx.fillRect(en.x - 17, en.y - en.size - 11, 34 * (en.hp / en.maxHp), 4);

                    ctx.fillStyle = "#f87171";
                    ctx.font = "11px sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(en.name + ` [${{en.nivel}}]`, en.x, en.y - en.size - 16);
                }});

                // Dibujar Jugador (Héroe con espada/armadura 2D simulada)
                ctx.fillStyle = "#eab308";
                ctx.beginPath();
                ctx.arc(player.x, player.y, player.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.lineWidth = 3;
                ctx.strokeStyle = "#ffffff";
                ctx.stroke();

                // Espada equipada sprite lateral
                ctx.fillStyle = "#cbd5e1";
                ctx.fillRect(player.x + 12, player.y - 4, 16, 6);

                ctx.fillStyle = "#facc15";
                ctx.font = "bold 13px 'Courier New', monospace";
                ctx.textAlign = "center";
                ctx.fillText("⭐ " + player.name, player.x, player.y - player.size - 10);
                
                ctx.restore();

                // DIBUJAR MINIMAPA CIRCULAR
                miniCtx.clearRect(0, 0, 120, 120);
                miniCtx.fillStyle = "#1e293b";
                miniCtx.fillRect(0, 0, 120, 120);
                
                // Escalar posición del jugador al minimapa
                let mX = (player.x / 5000) * 120;
                let mY = (player.y / 5000) * 120;
                
                // Enemigos en minimapa
                miniCtx.fillStyle = "#ef4444";
                enemies.forEach(en => {{
                    let ex = (en.x / 5000) * 120;
                    let ey = (en.y / 5000) * 120;
                    miniCtx.fillRect(ex-1, ey-1, 2, 2);
                }});

                // Jugador en minimapa
                miniCtx.fillStyle = "#facc15";
                miniCtx.beginPath();
                miniCtx.arc(mX, mY, 3, 0, Math.PI*2);
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