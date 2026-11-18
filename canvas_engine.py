# --- MOTOR HTML5 / JS CANVAS DE MUNDO ABIERTO (GEOGRAFÍA COMPLETA Y DETALLADA) ---

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
            body {{ background-color: #05070a; color: white; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; overflow: hidden; }}
            #gameContainer {{ position: relative; width: 100vw; height: 90vh; }}
            canvas {{ background: #0c1220; display: block; width: 100%; height: 100%; cursor: crosshair; }}
            .hud-overlay {{
                position: absolute; top: 15px; left: 20px; right: 20px;
                display: flex; justify-content: space-between; align-items: center;
                background: rgba(11, 15, 25, 0.9); padding: 12px 25px; border-radius: 10px;
                border: 1px solid #ffaa00; font-weight: bold; font-size: 15px; color: #ffaa00;
                pointer-events: none; box-shadow: 0 8px 24px rgba(0,0,0,0.7);
                backdrop-filter: blur(5px);
            }}
            .controls-hint {{
                position: absolute; bottom: 15px; left: 50%; transform: translateX(-50%);
                background: rgba(11, 15, 25, 0.9); padding: 8px 20px; border-radius: 8px;
                font-size: 13px; color: #b0b0b0; border: 1px solid #444; pointer-events: none;
                box-shadow: 0 4px 12px rgba(0,0,0,0.5);
            }}
        </style>
    </head>
    <body>
        <div id="gameContainer">
            <div class="hud-overlay">
                <span id="playerHpText">❤️ HP: 100/100</span>
                <span>🗺️ Región: {zona_actual}</span>
                <span id="scoreText">⚔️ Derrotados: 0</span>
                <span id="coordsText">📍 X: 2000 | Y: 2000</span>
            </div>
            <canvas id="gameCanvas"></canvas>
            <div class="controls-hint">Usa <b>W, A, S, D</b> o <b>Flechas</b> para moverte por el vasto mundo. Explora montañas, ríos, castillos, puertos y ciudades.</div>
        </div>
        
        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            
            function resizeCanvas() {{
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight * 0.90;
            }}
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();

            let player = {{ x: 2000, y: 2000, size: 24, speed: 5.5, hp: 100, maxHp: 100, color: "#ffaa00" }};
            let keys = {{}};
            let enemies = [];
            
            // Asentamientos, Castillos, Ciudades y Puertos en el mapa de 5000x5000
            let locations = [
                {{ x: 1800, y: 1900, name: "Aurelia Capital", type: "Ciudad Real", color: "#3498db", radius: 70 }},
                {{ x: 2900, y: 1100, name: "Sylvanis Refugio", type: "Ciudad Élfica", color: "#2ecc71", radius: 65 }},
                {{ x: 1100, y: 2900, name: "Khazad Dun Baluarte", type: "Fortaleza / Castillo", color: "#e67e22", radius: 75 }},
                {{ x: 3300, y: 3300, name: "Garra de la Tormenta", type: "Asentamiento Bestia", color: "#e74c3c", radius: 60 }},
                {{ x: 800, y: 1200, name: "Puerto del Sol", type: "Puerto Marítimo", color: "#00bcd4", radius: 55 }},
                {{ x: 4000, y: 2200, name: "Castillo de Hojacero", type: "Castillo Fortificado", color: "#9c27b0", radius: 70 }}
            ];

            // Generación fija de elementos geográficos (Montañas, Ríos, Bosques, Puertos)
            let mountains = [
                {{x: 1500, y: 800, r: 120}, {{x: 1700, y: 750, r: 150}, {{x: 2200, y: 900, r: 180},
                {{x: 3500, y: 1500, r: 200}, {{x: 3700, y: 1300, r: 160}, {{x: 2000, y: 3500, r: 220},
                {{x: 800, y: 3800, r: 190}, {{x: 3000, y: 2800, r: 170}
            ];

            let forests = [
                {{x: 2500, y: 1800, r: 250}, {{x: 1200, y: 2000, r: 220}, {{x: 3100, y: 2500, r: 200},
                {{x: 1500, y: 3200, r: 230}, {{x: 3500, y: 800, r: 180}
            ];

            let rivers = [
                [{x: 1800, y: 1900}, {x: 1500, y: 2200}, {x: 1200, y: 2800}, {x: 800, y: 1200}],
                [{x: 2900, y: 1100}, {x: 3200, y: 1800}, {x: 3500, y: 2500}, {x: 4000, y: 3500}],
                [{x: 2000, y: 2000}, {x: 2500, y: 2800}, {x: 3000, y: 3300}, {x: 3300, y: 3300}]
            ];

            let templateMobs = {str(mobs_js_data)};
            let derrotadosCount = 0;
            
            for(let i=0; i < 45; i++) {{
                let tmpl = templateMobs.length > 0 ? templateMobs[Math.floor(Math.random() * templateMobs.length)] : {{nombre: "Bestia Salvaje", hp: 100, ataque_tipo: "Físico", velocidad: 2}};
                enemies.push({{
                    x: Math.random() * 4600 + 200,
                    y: Math.random() * 4600 + 200,
                    size: 20,
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
                
                player.x = Math.max(80, Math.min(4920, player.x));
                player.y = Math.max(80, Math.min(4920, player.y));
                
                document.getElementById("coordsText").innerText = `📍 X: ${{Math.round(player.x)}} | Y: ${{Math.round(player.y)}}`;

                enemies.forEach(en => {{
                    let edx = player.x - en.x;
                    let edy = player.y - en.y;
                    let dist = Math.sqrt(edx*edx + edy*edy);
                    
                    if (dist < 450 && dist > 18) {{
                        en.x += (edx / dist) * en.speed;
                        en.y += (edy / dist) * en.speed;
                    }}
                    
                    en.cooldown++;
                    if (dist < 35 && en.cooldown > 55) {{
                        en.cooldown = 0;
                        let damage = Math.floor(Math.random() * 12) + 8;
                        player.hp -= damage;
                        if (player.hp < 0) player.hp = 0;
                        document.getElementById("playerHpText").innerText = `❤️ HP: ${{player.hp}}/${{player.maxHp}} [¡DAÑO!]`;
                    }}
                }});
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.save();
                let camX = canvas.width / 2 - player.x;
                let camY = canvas.height / 2 - player.y;
                ctx.translate(camX, camY);
                
                // 1. MAR Y OCÉANO DE FONDO (Bordes del mapa)
                ctx.fillStyle = "#091428";
                ctx.fillRect(0, 0, 5000, 5000);

                // Tierra continental principal
                ctx.fillStyle = "#111827";
                ctx.fillRect(300, 300, 4400, 4400);

                // 2. RÍOS
                ctx.strokeStyle = "#1ca3ec";
                ctx.lineWidth = 8;
                ctx.lineCap = "round";
                rivers.forEach(path => {{
                    ctx.beginPath();
                    ctx.moveTo(path[0].x, path[0].y);
                    for(let i=1; i<path.length; i++) {{
                        ctx.lineTo(path[i].x, path[i].y);
                    }}
                    ctx.stroke();
                }});

                // 3. BOSQUES Y ÁRBOLES
                ctx.fillStyle = "#143825";
                forests.forEach(f => {{
                    ctx.beginPath();
                    ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2);
                    ctx.fill();
                    // Detalles de copas de árboles
                    ctx.fillStyle = "#1e5631";
                    ctx.beginPath();
                    ctx.arc(f.x - 30, f.y - 20, f.r * 0.6, 0, Math.PI * 2);
                    ctx.arc(f.x + 40, f.y + 20, f.r * 0.5, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.fillStyle = "#143825";
                }});

                // 4. MONTAÑAS
                ctx.fillStyle = "#374151";
                mountains.forEach(m => {{
                    ctx.beginPath();
                    ctx.arc(m.x, m.y, m.r, 0, Math.PI * 2);
                    ctx.fill();
                    // Picos rocosos
                    ctx.fillStyle = "#4b5563";
                    ctx.beginPath();
                    ctx.moveTo(m.x, m.y - m.r);
                    ctx.lineTo(m.x - m.r * 0.7, m.y + m.r * 0.5);
                    ctx.lineTo(m.x + m.r * 0.7, m.y + m.r * 0.5);
                    ctx.closePath();
                    ctx.fill();
                    ctx.fillStyle = "#374151";
                }});

                // 5. CAMINOS Y RUTAS
                ctx.strokeStyle = "#78350f";
                ctx.lineWidth = 6;
                ctx.setLineDash([15, 10]);
                ctx.beginPath();
                ctx.moveTo(1800, 1900); ctx.lineTo(2900, 1100);
                ctx.moveTo(1800, 1900); ctx.lineTo(1100, 2900);
                ctx.moveTo(2900, 1100); ctx.lineTo(3300, 3300);
                ctx.moveTo(1100, 2900); ctx.lineTo(800, 1200);
                ctx.stroke();
                ctx.setLineDash([]); // reset

                // 6. CIUDADES, CASTILLOS Y PUERTOS
                locations.forEach(loc => {{
                    let grad = ctx.createRadialGradient(loc.x, loc.y, 5, loc.x, loc.y, loc.radius);
                    grad.addColorStop(0, loc.color);
                    grad.addColorStop(1, "rgba(17, 24, 39, 0.8)");
                    
                    ctx.fillStyle = grad;
                    ctx.beginPath();
                    ctx.arc(loc.x, loc.y, loc.radius, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.lineWidth = 3;
                    ctx.strokeStyle = loc.color;
                    ctx.stroke();

                    // Icono de asentamiento / castillo
                    ctx.fillStyle = "#ffffff";
                    ctx.font = "bold 15px 'Segoe UI', sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(loc.name, loc.x, loc.y - loc.radius - 14);
                    
                    ctx.font = "12px 'Segoe UI', sans-serif";
                    ctx.fillStyle = "#cbd5e1";
                    ctx.fillText("[" + loc.type + "]", loc.x, loc.y - loc.radius - 2);
                }});

                // 7. ENEMIGOS HOSTILES (IA ACTIVA)
                enemies.forEach(en => {{
                    ctx.shadowColor = "#ff0000";
                    ctx.shadowBlur = 12;
                    ctx.fillStyle = en.color;
                    ctx.beginPath();
                    ctx.arc(en.x, en.y, en.size, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.shadowBlur = 0;
                    
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = "#ffffff";
                    ctx.stroke();
                    
                    ctx.fillStyle = "#ffbbbb";
                    ctx.font = "11px sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(en.name + ` [Nv.${{en.nivel}}]`, en.x, en.y - en.size - 6);
                }});
                
                // 8. TU JUGADOR (HÉROE)
                ctx.shadowColor = "#ffaa00";
                ctx.shadowBlur = 18;
                ctx.fillStyle = player.color;
                ctx.beginPath();
                ctx.arc(player.x, player.y, player.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 0;
                
                ctx.lineWidth = 3;
                ctx.strokeStyle = "#ffffff";
                ctx.stroke();

                ctx.fillStyle = "#ffcc00";
                ctx.font = "bold 14px 'Segoe UI', sans-serif";
                ctx.fillText("⭐ Tu Héroe", player.x, player.y - player.size - 10);
                
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