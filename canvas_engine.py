# --- MOTOR HTML5 / JS CANVAS — MMORPG 2D CON NPCs PLEBEYOS, MISIONES OCULTAS Y OBJETOS MÍTICOS ---

def generar_canvas_html(es_caza, zona_actual, mobs_zona, jefes_zona):
    mobs_js_data = []
    for m in mobs_zona:
        mobs_js_data.append({
            "nombre": m["nombre"],
            "nivel": m["nivel"],
            "hp": m["hp"],
            "ataque_tipo": m["ataque"],
            "velocidad": m.get("velocidad", 1.8),
            "tipo": m.get("tipo", "goblin")
        })

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ background-color: #05080f; color: #fff; margin: 0; padding: 0; overflow: hidden; font-family: 'Segoe UI', Tahoma, sans-serif; user-select: none; }}
            #gameContainer {{ position: relative; width: 100vw; height: 92vh; }}
            canvas {{ background: #1a2e12; display: block; width: 100%; height: 100%; cursor: crosshair; }}
            
            /* HUD Superior tipo MMORPG */
            .mmorpg-top-hud {{
                position: absolute; top: 12px; left: 15px; right: 15px;
                display: flex; justify-content: space-between; align-items: center;
                pointer-events: none; z-index: 10;
            }}
            .player-frame {{
                background: rgba(15, 23, 42, 0.92); border: 2px solid #b45309; padding: 10px 18px;
                border-radius: 8px; box-shadow: 0 6px 16px rgba(0,0,0,0.8); display: flex; flex-direction: column; gap: 5px;
                pointer-events: auto;
            }}
            .hp-bar-bg {{ width: 200px; height: 14px; background: #450a0a; border: 1px solid #7f1d1d; border-radius: 4px; overflow: hidden; }}
            .hp-bar-fill {{ width: 100%; height: 100%; background: #dc2626; transition: width 0.2s ease-in-out; }}
            
            .minimap-frame {{
                width: 140px; height: 140px; background: rgba(15, 23, 42, 0.92);
                border: 3px solid #d97706; border-radius: 50%; box-shadow: 0 6px 20px rgba(0,0,0,0.85);
                display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;
            }}
            
            /* Menú lateral de Acceso Rápido MMORPG */
            .mmorpg-side-menu {{
                position: absolute; top: 170px; right: 20px;
                display: flex; flex-direction: column; gap: 10px; z-index: 10;
                pointer-events: auto;
            }}
            .menu-btn {{
                background: rgba(15, 23, 42, 0.95); border: 2px solid #b45309; color: #facc15;
                padding: 10px 15px; border-radius: 8px; font-weight: bold; cursor: pointer;
                box-shadow: 0 4px 12px rgba(0,0,0,0.7); font-size: 13px; text-align: left;
                transition: all 0.2s;
            }}
            .menu-btn:hover {{ background: #b45309; color: #fff; transform: translateX(-4px); }}

            /* Ventana Modal de Interacción NPC / Misiones Míticas */
            #npcModal {{
                position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
                width: 480px; background: rgba(15, 23, 42, 0.98); border: 3px solid #d97706;
                border-radius: 12px; padding: 25px; box-shadow: 0 12px 40px rgba(0,0,0,0.9);
                display: none; z-index: 100; text-align: center;
            }}
            #npcModal h2 {{ color: #f59e0b; margin-top: 0; font-size: 20px; }}
            #npcModal p {{ color: #cbd5e1; font-size: 14px; line-height: 1.6; }}
            .modal-btn-group {{ display: flex; justify-content: center; gap: 12px; margin-top: 20px; }}
            .modal-accept {{ background: #d97706; color: white; border: none; padding: 8px 18px; border-radius: 6px; font-weight: bold; cursor: pointer; }}
            .modal-close {{ background: #475569; color: white; border: none; padding: 8px 18px; border-radius: 6px; font-weight: bold; cursor: pointer; }}

            /* Barra de Acciones Rápida Inferior */
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

            .interaction-prompt {{
                position: absolute; bottom: 90px; left: 50%; transform: translateX(-50%);
                background: rgba(0,0,0,0.85); border: 1px solid #f59e0b; color: #facc15;
                padding: 6px 16px; border-radius: 6px; font-size: 13px; font-weight: bold;
                display: none; pointer-events: none; z-index: 50; box-shadow: 0 4px 12px rgba(0,0,0,0.6);
            }}
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

            <div class="mmorpg-side-menu">
                <button class="menu-btn" onclick="alert('📜 Misiones Activas:\\n- Rumores de la calle (Habla con plebeyos)\\n- El Secreto del Ermitaje (Misión Mítica)')">📜 Misiones</button>
                <button class="menu-btn" onclick="alert('🎒 Inventario: Ropa de Viajero, Raciones (x3), Fragmento Mítico (0/3)')">🎒 Inventario</button>
                <button class="menu-btn" onclick="alert('⚡ Habilidades: Invocación de Golem de Roca (Equipada)')">⚡ Habilidades</button>
                <button class="menu-btn" onclick="alert('👑 Tratados y Reputación:\\n- Reino de Valoria: Respetado (60/100)\\n- Faction Mítica: Desconocida')">👑 Tratados</button>
            </div>

            <div id="interactionPrompt" class="interaction-prompt">Presiona <b>E</b> para hablar</div>

            <!-- Ventana Modal de NPC y Misiones Ocultas -->
            <div id="npcModal">
                <h2 id="npcTitle">Título NPC</h2>
                <p id="npcText">Diálogo del NPC...</p>
                <div class="modal-btn-group">
                    <button class="modal-accept" id="modalAcceptBtn" onclick="acceptSecretQuest()">Aceptar Misión Mítica</button>
                    <button class="modal-close" onclick="closeNpcModal()">Cerrar</button>
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

            let player = {{ x: 2500, y: 2500, radius: 18, speed: 5, hp: 100, maxHp: 100, name: "Héroe" }};
            let keys = {{}};
            let enemies = [];
            
            // Estructuras con colisión
            let structures = [
                {{ x: 2300, y: 2300, w: 260, h: 200, name: "Aurelia Capital", type: "city" }},
                {{ x: 3400, y: 1400, w: 220, h: 220, name: "Castillo de Hojacero", type: "castle" }},
                {{ x: 1300, y: 3100, w: 200, h: 180, name: "Baluarte Enano", type: "fortress" }},
                {{ x: 900, y: 1100, w: 180, h: 160, name: "Puerto Marítimo", type: "port" }}
            ];

            let scenery = [];
            for(let i=0; i<100; i++) {{
                scenery.push({{
                    x: Math.random() * 4700 + 150,
                    y: Math.random() * 4700 + 150,
                    type: Math.random() > 0.4 ? 'tree' : 'rock',
                    radius: 22
                }});
            }}

            // NPCs: Plebeyos callejeros (patrullan) y NPCs Ocultos de Misiones Míticas
            let npcs = [
                {{ x: 2380, y: 2380, name: "Aldric (Maestro de Misiones)", radius: 16, type: "quest", dialog: "¡Bienvenido a Aurelia Capital! Las bestias acechan en las afueras." }},
                {{ x: 3500, y: 1500, name: "Herrero Bran", radius: 16, type: "merchant", dialog: "¿Necesitas afilar tu espada o forjar equipo? Pásate por la forja real." }},
                // Plebeyos callejeros
                {{ x: 2420, y: 2400, name: "Ciudadano de Aurelia", radius: 14, type: "plebeian", dialog: "Dicen que el viejo ermitaje del bosque esconde secretos de armas legendarias..." }},
                {{ x: 2350, y: 2450, name: "Mercader Callejero", radius: 14, type: "plebeian", dialog: "¡Comida fresca y rumores baratos! ¿Has oído hablar de las reliquias míticas?" }},
                {{ x: 2480, y: 2350, name: "Guardia Real", radius: 14, type: "plebeian", dialog: "Mantén el orden en las calles, aventurero. No queremos problemas aquí." }},
                // NPC Oculto para Misión Mítica
                {{ x: 1200, y: 1200, name: "Ermitaje Oculto: Maestro Ignis", radius: 16, type: "mythic_quest", dialog: "Has encontrado mi refugio secreto. Si buscas la hoja mítica 'Sol Invictus', debes derrotar al Guardián de las Sombras en las profundidades y traerme su núcleo estelar." }}
            ];

            let mobTypes = ["Goblin", "Lobo de Pradera", "Bandido", "Ent Corrupto"];
            let templateMobs = {str(mobs_js_data)};
            for(let i=0; i < 45; i++) {{
                let mName = mobTypes[Math.floor(Math.random() * mobTypes.length)];
                let hpVal = mName === "Ent Corrupto" ? 140 : 70;
                enemies.push({{
                    x: Math.random() * 4600 + 200, y: Math.random() * 4600 + 200,
                    radius: 18, speed: 1.8, hp: hpVal, maxHp: hpVal,
                    name: mName, nivel: Math.floor(Math.random() * 5) + 1, cooldown: 0
                }});
            }}
            
            window.addEventListener("keydown", (e) => keys[e.key] = true);
            window.addEventListener("keyup", (e) => keys[e.key] = false);

            let activeNpc = null;

            function checkCollision(nx, ny, radius) {{
                for(let st of structures) {{
                    if (nx + radius > st.x && nx - radius < st.x + st.w &&
                        ny + radius > st.y && ny - radius < st.y + st.h) return true;
                }}
                for(let sc of scenery) {{
                    let dx = nx - sc.x, dy = ny - sc.y;
                    if (Math.sqrt(dx*dx + dy*dy) < radius + sc.radius * 0.7) return true;
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

                player.x = Math.max(60, Math.min(4940, player.x));
                player.y = Math.max(60, Math.min(4940, player.y));

                // Proximidad con NPCs
                let nearNpc = null;
                npcs.forEach(npc => {{
                    let ndx = player.x - npc.x, ndy = player.y - npc.y;
                    if (Math.sqrt(ndx*ndx + ndy*ndy) < 45) {{
                        nearNpc = npc;
                    }}
                }});

                if (nearNpc) {{
                    document.getElementById("interactionPrompt").style.display = "block";
                    if (keys["e"] || keys["E"]) {{
                        activeNpc = nearNpc;
                        openNpcModal(nearNpc.name, nearNpc.dialog, nearNpc.type);
                    }}
                }} else {{
                    document.getElementById("interactionPrompt").style.display = "none";
                }}

                // IA Enemigos
                enemies.forEach(en => {{
                    let edx = player.x - en.x, edy = player.y - en.y;
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

            function openNpcModal(title, text, type) {{
                document.getElementById("npcTitleinnerText") = title;
                document.getElementById("npcTitle").innerText = title;
                document.getElementById("npcText").innerText = text;
                let btnAcc = document.getElementById("modalAcceptBtn");
                if (type === 'mythic_quest') {{
                    btnAcc.style.display = "inline-block";
                    btnAcc.innerText = "Aceptar Misión Mítica";
                }} else {{
                    btnAcc.style.display = "none";
                }}
                document.getElementById("npcModal").style.display = "block";
            }}

            function closeNpcModal() {{
                document.getElementById("npcModal").style.display = "none";
            }}

            function acceptSecretQuest() {{
                alert(" ¡Misión Mítica aceptada! Busca pistas en las zonas profundas del mapa para forjar tu arma mítica.");
                closeNpcModal();
            }}

            function drawPlayerSprite(x, y) {{
                ctx.save();
                ctx.translate(x, y);
                ctx.fillStyle = "rgba(0,0,0,0.5)";
                ctx.beginPath(); ctx.ellipse(0, 14, 12, 6, 0, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = "#1e3a8a"; ctx.fillRect(-9, -9, 18, 20);
                ctx.fillStyle = "#fde047"; ctx.beginPath(); ctx.arc(0, -10, 9, 0, Math.PI * 2); ctx.fill();
                ctx.strokeStyle = "#ca8a04"; ctx.lineWidth = 2; ctx.stroke();
                ctx.fillStyle = "#e2e8f0"; ctx.fillRect(10, -5, 4, 16);
                ctx.restore();
            }}

            function drawMonsterSprite(x, y, name) {{
                ctx.save();
                ctx.translate(x, y);
                ctx.fillStyle = "rgba(0,0,0,0.5)";
                ctx.beginPath(); ctx.ellipse(0, 12, 10, 5, 0, 0, Math.PI * 2); ctx.fill();

                let colorM = name === "Ent Corrupto" ? "#14532d" : (name === "Bandido" ? "#581c87" : "#7f1d1d");
                ctx.fillStyle = colorM; ctx.beginPath(); ctx.roundRect(-12, -12, 24, 24, [6]); ctx.fill();
                ctx.strokeStyle = "#ef4444"; ctx.lineWidth = 2; ctx.stroke();
                ctx.fillStyle = "#facc15"; ctx.fillRect(-5, -5, 3, 3); ctx.fillRect(2, -5, 3, 3);
                ctx.restore();
            }}

            function drawNpcSprite(x, y, name, type) {{
                ctx.save();
                ctx.translate(x, y);
                ctx.fillStyle = "rgba(0,0,0,0.5)";
                ctx.beginPath(); ctx.ellipse(0, 12, 10, 5, 0, 0, Math.PI * 2); ctx.fill();

                let colorN = type === 'mythic_quest' ? "#9333ea" : (type === 'plebeian' ? "#0284c7" : "#047857");
                ctx.fillStyle = colorN; ctx.fillRect(-9, -9, 18, 20);
                ctx.fillStyle = "#fde047"; ctx.beginPath(); ctx.arc(0, -10, 9, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = type === 'mythic_quest' ? "#facc15" : "#ffffff";
                ctx.font = "bold 11px sans-serif";
                ctx.textAlign = "center";
                ctx.fillText(type === 'mythic_quest' ? "⭐ " + name.split(" ")[0] : "💬 " + name.split(" ")[0], 0, -22);
                ctx.restore();
            }}
            
            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.save();
                
                let camX = canvas.width / 2 - player.x;
                let camY = canvas.height / 2 - player.y;
                ctx.translate(camX, camY);
                
                ctx.fillStyle = "#1a2e12";
                ctx.fillRect(0, 0, 5000, 5000);

                structures.forEach(st => {{
                    ctx.fillStyle = "#334155"; ctx.fillRect(st.x, st.y, st.w, st.h);
                    ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 4; ctx.strokeRect(st.x, st.y, st.w, st.h);
                    ctx.fillStyle = "#991b1b"; ctx.fillRect(st.x - 12, st.y - 25, st.w + 24, 28);
                    ctx.fillStyle = "#ffffff"; ctx.font = "bold 16px 'Segoe UI', sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(st.name, st.x + st.w/2, st.y - 35);
                }});

                npcs.forEach(npc => {{
                    drawNpcSprite(npc.x, npc.y, npc.name, npc.type);
                }});

                scenery.forEach(sc => {{
                    ctx.fillStyle = "rgba(0,0,0,0.3)";
                    ctx.beginPath(); ctx.ellipse(sc.x, sc.y + 10, sc.radius * 0.7, sc.radius * 0.3, 0, 0, Math.PI*2); ctx.fill();

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
                ctx.fillStyle = "#facc15"; ctx.font = "bold 13px 'Segoe UI', sans-serif"; ctx.textAlign = "center";
                ctx.fillText("⭐ " + player.name, player.x, player.y - 26);
                
                ctx.restore();

                miniCtx.clearRect(0, 0, 130, 130);
                miniCtx.fillStyle = "#0f172a"; miniCtx.fillRect(0, 0, 130, 130);
                
                let mX = (player.x / 5000) * 130, mY = (player.y / 5000) * 130;
                enemies.forEach(en => {{
                    let ex = (en.x / 5000) * 130, ey = (en.y / 5000) * 130;
                    miniCtx.fillStyle = "#ef4444"; miniCtx.fillRect(ex-1, ey-1, 2, 2);
                }});
                npcs.forEach(npc => {{
                    let nx = (npc.x / 5000) * 130, ny = (npc.y / 5000) * 130;
                    miniCtx.fillStyle = npc.type === 'mythic_quest' ? "#facc15" : "#10b981";
                    miniCtx.fillRect(nx-2, ny-2, 4, 4);
                }});
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