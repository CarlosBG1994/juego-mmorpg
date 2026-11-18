# --- MOTOR HTML5 / JS CANVAS PARA PVE EN TIEMPO REAL ---

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
            body {{ background-color: #0e1117; color: white; text-align: center; font-family: sans-serif; margin: 0; padding: 0; }}
            canvas {{ background: #1a1c23; border: 2px solid #ffaa00; box-shadow: 0 0 20px rgba(255,170,0,0.4); border-radius: 8px; }}
            .hud-game {{ display: flex; justify-content: space-around; background: #161922; padding: 8px; margin-bottom: 5px; border-radius: 5px; font-weight: bold; font-size: 13px; color: #ffaa00; }}
            .controls-hint {{ font-size: 12px; color: #a0a0a0; margin-top: 5px; }}
        </style>
    </head>
    <body>
        <div class="hud-game">
            <span id="playerHpText">❤️ HP: 100/100</span>
            <span id="zoneText">🗺️ Zona: {zona_actual}</span>
            <span id="scoreText">⚔️ Derrotados: 0</span>
        </div>
        <canvas id="gameCanvas" width="800" height="380"></canvas>
        <div class="controls-hint">Usa las teclas <b>W, A, S, D</b> o <b>Flechas</b> para moverte y esquivar ataques mágicos y físicos en tiempo real.</div>
        
        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            
            let player = {{ x: 400, y: 190, size: 20, speed: 4, hp: 100, maxHp: 100, color: "#ffaa00" }};
            let keys = {{}};
            let enemies = [];
            let projectiles = [];
            let isCaza = {str(es_caza).lower()};
            
            let templateMobs = {str(mobs_js_data)};
            
            if (isCaza && templateMobs.length > 0) {{
                for(let i=0; i<4; i++) {{
                    let tmpl = templateMobs[Math.floor(Math.random() * templateMobs.length)];
                    enemies.push({{
                        x: Math.random() * 700 + 50,
                        y: Math.random() * 300 + 40,
                        size: 18,
                        speed: tmpl.velocidad || 1.5,
                        hp: tmpl.hp,
                        maxHp: tmpl.hp,
                        name: tmpl.nombre,
                        ataque_tipo: tmpl.ataque_tipo,
                        cooldown: 0,
                        color: tmpl.ataque_tipo.includes("Magia") ? "#9933ff" : "#ff4444"
                    }});
                }}
            }}
            
            window.addEventListener("keydown", (e) => keys[e.key] = true);
            window.addEventListener("keyup", (e) => keys[e.key] = false);
            
            function update() {{
                if (keys["ArrowUp"] || keys["w"] || keys["W"]) player.y -= player.speed;
                if (keys["ArrowDown"] || keys["s"] || keys["S"]) player.y += player.speed;
                if (keys["ArrowLeft"] || keys["a"] || keys["A"]) player.x -= player.speed;
                if (keys["ArrowRight"] || keys["d"] || keys["D"]) player.x += player.speed;
                
                player.x = Math.max(player.size, Math.min(canvas.width - player.size, player.x));
                player.y = Math.max(player.size, Math.min(canvas.height - player.size, player.y));
                
                if (isCaza) {{
                    enemies.forEach(en => {{
                        let dx = player.x - en.x;
                        let dy = player.y - en.y;
                        let dist = Math.sqrt(dx*dx + dy*dy);
                        
                        if (dist > 2) {{
                            en.x += (dx / dist) * en.speed;
                            en.y += (dy / dist) * en.speed;
                        }}
                        
                        en.cooldown++;
                        if (en.cooldown > 100 && dist < 200) {{
                            en.cooldown = 0;
                            if (en.ataque_tipo.includes("Magia")) {{
                                projectiles.push({{
                                    x: en.x, y: en.y,
                                    vx: (dx / dist) * 3,
                                    vy: (dy / dist) * 3,
                                    radius: 6,
                                    color: "#9933ff"
                                }});
                            }} else if (dist < 30) {{
                                let isCrit = Math.random() < 0.15;
                                let damage = isCrit ? 25 : 12;
                                player.hp -= damage;
                                if (player.hp < 0) player.hp = 0;
                                document.getElementById("playerHpText").innerText = `❤️ HP: ${{player.hp}}/${{player.maxHp}}` + (isCrit ? " [¡CRÍTICO RECIBIDO!]" : "");
                            }}
                        }}
                    }});
                    
                    for(let i = projectiles.length - 1; i >= 0; i--) {{
                        let p = projectiles[i];
                        p.x += p.vx;
                        p.y += p.vy;
                        
                        let pdx = player.x - p.x;
                        let pdy = player.y - p.y;
                        if (Math.sqrt(pdx*pdx + pdy*pdy) < player.size + p.radius) {{
                            let isCrit = Math.random() < 0.2;
                            let dmg = isCrit ? 30 : 15;
                            player.hp -= dmg;
                            if (player.hp < 0) player.hp = 0;
                            projectiles.splice(i, 1);
                            document.getElementById("playerHpText").innerText = `❤️ HP: ${{player.hp}}/${{player.maxHp}}` + (isCrit ? " [¡CRÍTICO MÁGICO!]" : "");
                            continue;
                        }}
                        
                        if (p.x < 0 || p.x > canvas.width || p.y < 0 || p.y > canvas.height) {{
                            projectiles.splice(i, 1);
                        }}
                    }}
                }}
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                ctx.strokeStyle = "#252836";
                ctx.lineWidth = 1;
                for(let x=0; x<canvas.width; x+=40) {{
                    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
                }}
                for(let y=0; y<canvas.height; y+=40) {{
                    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
                }}
                
                ctx.fillStyle = player.color;
                ctx.beginPath();
                ctx.arc(player.x, player.y, player.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.lineWidth = 3;
                ctx.strokeStyle = "#ffffff";
                ctx.stroke();
                
                enemies.forEach(en => {{
                    ctx.fillStyle = en.color;
                    ctx.beginPath();
                    ctx.arc(en.x, en.y, en.size, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = "#ffffff";
                    ctx.stroke();
                    
                    ctx.fillStyle = "#ffffff";
                    ctx.font = "10px sans-serif";
                    ctx.fillText(en.name, en.x - 20, en.y - en.size - 6);
                }});
                
                projectiles.forEach(p => {{
                    ctx.fillStyle = p.color;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                    ctx.fill();
                }});
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