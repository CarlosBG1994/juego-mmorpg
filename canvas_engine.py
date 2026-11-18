# --- MOTOR HTML5 / JS CANVAS DE MUNDO ABIERTO A PANTALLA COMPLETA ---

def generar_canvas_html(es_caza, zona_actual, mobs_zona, jefes_zona):
    mobs_js_data = []
    for m in mobs_zona:
        mobs_js_data.append({
            "nombre": m["nombre"],
            "nivel": m["nivel"],
            "hp": m["hp"],
            "ataque_tipo": m["ataque"],
            "velocidad": m.get("velocidad", 1.5)
        })

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ background-color: #0b0e14; color: white; text-align: center; font-family: sans-serif; margin: 0; padding: 0; overflow: hidden; }}
            #gameContainer {{ position: relative; width: 100vw; height: 85vh; }}
            canvas {{ background: #121620; display: block; width: 100%; height: 100%; cursor: crosshair; }}
            .hud-overlay {{
                position: absolute; top: 10px; left: 10px; right: 10px;
                display: flex; justify-content: space-between; align-items: center;
                background: rgba(18, 22, 32, 0.85); padding: 10px 20px; border-radius: 8px;
                border: 1px solid #ffaa00; font-weight: bold; font-size: 14px; color: #ffaa00;
                pointer-events: none; box-shadow: 0 4px 12px rgba(0,0,0,0.5);
            }}
            .controls-hint {{
                position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%);
                background: rgba(18, 22, 32, 0.85); padding: 6px 15px; border-radius: 5px;
                font-size: 12px; color: #a0a0a0; border: 1px solid #333; pointer-events: none;
            }}
        </style>
    </head>
    <body>
        <div id="gameContainer">
            <div class="hud-overlay">
                <span id="playerHpText">❤️ HP: 100/100</span>
                <span>🗺️ Región: {zona_actual}</span>
                <span id="scoreText">⚔️ Derrotados: 0</span>
                <span id="coordsText">📍 X: 400 | Y: 300</span>
            </div>
            <canvas id="gameCanvas"></canvas>
            <div class="controls-hint">Usa <b>W, A, S, D</b> o <b>Flechas</b> para moverte por el vasto mundo. ¡Esquiva a los enemigos hostiles!</div>
        </div>
        
        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            
            function resizeCanvas() {{
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight * 0.85;
            }}
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();

            // Jugador y mundo masivo
            let player = {{ x: 2000, y: 2000, size: 22, speed: 5, hp: 100, maxHp: 100, color: "#ffaa00" }};
            let keys = {{}};
            let enemies = [];
            let settlements = [
                {{ x: 1800, y: 1900, name: "Aurelia Capital (Humano)", color: "#3498db", radius: 50 }},
                {{ x: 2800, y: 1200, name: "Sylvanis Refugio (Elfo)", color: "#2ecc71", radius: 50 }},
                {{ x: 1200, y: 2800, name: "Khazad Dun Baluarte (Enano)", color: "#e67e22", radius: 50 }},
                {{ x: 3200, y: 3200, name: "Garra de la Tormenta (Bestia)", color: "#e74c3c", radius: 50 }}
            ];
            
            let templateMobs = {str(mobs_js_data)};
            let derrotadosCount = 0;
            
            // Generar mobs distribuidos por el vasto mundo abierto (mapa de 5000x5000)
            for(let i=0; i < 40; i++) {{
                let tmpl = templateMobs.length > 0 ? templateMobs[Math.floor(Math.random() * templateMobs.length)] : {{nombre: "Bestia Salvaje", hp: 100, ataque_tipo: "Físico", velocidad: 2}};
                enemies.push({{
                    x: Math.random() * 4600 + 200,
                    y: Math.random() * 4600 + 200,
                    size: 18,
                    speed: tmpl.velocidad || 1.8,
                    hp: tmpl.hp,
                    maxHp: tmpl.hp,
                    name: tmpl.nombre,
                    ataque_tipo: tmpl.ataque_tipo,
                    cooldown: 0,
                    color: "#ff3333"
                }});
            }}
            
            window.addEventListener("keydown", (e) => keys[e.key] = true);
            window.addEventListener("keyup", (e) => keys[e.key] = false);
            
            function update() {{
                let dxInput = 0;
                let dyInput = 0;
                if (keys["ArrowUp"] || keys["w"] || keys["W"]) dyInput -= player.speed;
                if (keys["ArrowDown"] || keys["s"] || keys["S"]) dyInput += player.speed;
                if (keys["ArrowLeft"] || keys["a"] || keys["A"]) dxInput -= player.speed;
                if (keys["ArrowRight"] || keys["d"] || keys["D"]) dxInput += player.speed;
                
                player.x += dxInput;
                player.y += dyInput;
                
                // Limites del mundo masivo (5000x5000)
                player.x = Math.max(50, Math.min(4950, player.x));
                player.y = Math.max(50, Math.min(4950, player.y));
                
                document.getElementById("coordsText").innerText = `📍 X: ${{Math.round(player.x)}} | Y: ${{Math.round(player.y)}}`;

                // IA de Enemigos: persecución activa y daño en tiempo real
                enemies.forEach(en => {{
                    let edx = player.x - en.x;
                    let edy = player.y - en.y;
                    let dist = Math.sqrt(edx*edx + edy*edy);
                    
                    if (dist < 400 && dist > 15) {{
                        en.x += (edx / dist) * en.speed;
                        en.y += (edy / dist) * en.speed;
                    }}
                    
                    en.cooldown++;
                    if (dist < 30 && en.cooldown > 60) {{
                        en.cooldown = 0;
                        let damage = Math.floor(Math.random() * 10) + 8;
                        player.hp -= damage;
                        if (player.hp < 0) player.hp = 0;
                        document.getElementById("playerHpText").innerText = `❤️ HP: ${{player.hp}}/${{player.maxHp}} [¡GOLPE RECIBIDO!]`;
                    }}
                }});
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Camara centrada en el jugador
                ctx.save();
                let camX = canvas.width / 2 - player.x;
                let camY = canvas.height / 2 - player.y;
                ctx.translate(camX, camY);
                
                // Dibujar suelo y rejilla del mundo masivo
                ctx.strokeStyle = "#1e2330";
                ctx.lineWidth = 2;
                ctx.beginPath();
                for(let x=0; x<=5000; x+=200) {{
                    ctx.moveTo(x, 0); ctx.lineTo(x, 5000);
                }}
                for(let y=0; y<=5000; y+=200) {{
                    ctx.moveTo(0, y); ctx.lineTo(5000, y);
                }}
                ctx.stroke();

                // Dibujar Asentamientos y Ciudades en el mapa
                settlements.forEach(st => {{
                    ctx.fillStyle = st.color;
                    ctx.beginPath();
                    ctx.arc(st.x, st.y, st.radius, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.lineWidth = 4;
                    ctx.strokeStyle = "#ffffff";
                    ctx.stroke();

                    ctx.fillStyle = "#ffffff";
                    ctx.font = "bold 14px sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(st.name, st.x, st.y - st.radius - 10);
                }});

                // Dibujar Enemigos (círculos rojos con IA)
                enemies.forEach(en => {{
                    ctx.fillStyle = en.color;
                    ctx.beginPath();
                    ctx.arc(en.x, en.y, en.size, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = "#fff";
                    ctx.stroke();
                    
                    ctx.fillStyle = "#ff9999";
                    ctx.font = "11px sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(en.name + ` (Nv.${{en.nivel}})`, en.x, en.y - en.size - 6);
                }});
                
                // Dibujar Jugador
                ctx.fillStyle = player.color;
                ctx.beginPath();
                ctx.arc(player.x, player.y, player.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.lineWidth = 3;
                ctx.strokeStyle = "#ffffff";
                ctx.stroke();

                ctx.fillStyle = "#ffaa00";
                ctx.font = "bold 13px sans-serif";
                ctx.fillText("⭐ Héroe", player.x, player.y - player.size - 8);
                
                ctx.restore();
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