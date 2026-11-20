# --- MOTOR HTML5 / JS CANVAS (canvas_engine.py) ---
import json


def generar_canvas_html(
    continente_actual,
    zona_actual,
    montura_equipada,
    velocidad_base,
    estilo_cabello,
    color_armadura,
    mobs_zona,
    habilidades_equipadas,
):
    mobs_js = json.dumps(
        [
            {
                "nombre": m["nombre"],
                "nivel": m["nivel"],
                "hp": m["hp"],
                "ataque_tipo": m["ataque"],
                "velocidad": m.get("velocidad", 1.8),
            }
            for m in mobs_zona
        ],
        ensure_ascii=False,
    )

    skills_js = json.dumps(habilidades_equipadas, ensure_ascii=False)

    colores_armadura_map = {
        "Azul Real (Valoria)": "#2563eb",
        "Rojo Sangre": "#dc2626",
        "Verde Esmeralda": "#16a34a",
        "Dorado Divino": "#eab308",
        "Oscuro Abisal": "#475569",
    }
    color_hex = colores_armadura_map.get(color_armadura, "#2563eb")

    s1 = habilidades_equipadas["1"]
    s2 = habilidades_equipadas["2"]
    s3 = habilidades_equipadas["3"]
    s4 = habilidades_equipadas["4"]
    sq = habilidades_equipadas["q"]

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <style>
            body {{ background-color: #020617; color: #fff; margin: 0; padding: 0; overflow: hidden; font-family: 'Segoe UI', Tahoma, sans-serif; user-select: none; }}
            #gameContainer {{ position: relative; width: 100vw; height: 92vh; }}
            canvas {{ background: #0284c7; display: block; width: 100%; height: 100%; cursor: crosshair; }}
            
            .mmorpg-top-hud {{
                position: absolute; top: 12px; left: 15px; right: 15px;
                display: flex; justify-content: space-between; align-items: flex-start;
                pointer-events: none; z-index: 10;
            }}
            .player-frame {{
                background: rgba(15, 23, 42, 0.95); border: 2px solid #b45309; padding: 10px 18px;
                border-radius: 8px; box-shadow: 0 6px 16px rgba(0,0,0,0.8); display: flex; flex-direction: column; gap: 4px;
                pointer-events: auto;
            }}
            .hp-bar-bg {{ width: 220px; height: 14px; background: #450a0a; border: 1px solid #7f1d1d; border-radius: 4px; overflow: hidden; }}
            .hp-bar-fill {{ width: 100%; height: 100%; background: #22c55e; transition: width 0.2s ease-in-out; }}
            
            .minimap-frame {{
                width: 145px; height: 145px; background: rgba(15, 23, 42, 0.95);
                border: 3px solid #d97706; border-radius: 50%; box-shadow: 0 6px 20px rgba(0,0,0,0.85);
                display: flex; align-items: center; justify-content: center; position: relative; overflow: hidden;
            }}
            
            .mmorpg-action-bar {{
                position: absolute; bottom: 16px; left: 50%; transform: translateX(-50%);
                background: rgba(15, 23, 42, 0.95); border: 2px solid #78350f; padding: 8px 14px;
                border-radius: 10px; display: flex; gap: 10px; pointer-events: auto; z-index: 10;
            }}
            .action-slot {{
                width: 68px; height: 64px; background: #1e293b; border: 2px solid #475569;
                border-radius: 6px; display: flex; flex-direction: column; align-items: center; justify-content: center;
                font-size: 18px; font-weight: bold; color: #facc15; position: relative; cursor: pointer; padding: 2px;
            }}
            .action-slot .slot-name {{
                font-size: 9px; color: #e2e8f0; text-align: center; line-height: 1.05;
                max-width: 62px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; margin-top: 2px;
            }}
            .action-slot .slot-key {{ font-size: 10px; color: #facc15; position: absolute; top: 2px; left: 5px; }}
            
            .combat-hint {{
                position: absolute; bottom: 96px; left: 50%; transform: translateX(-50%);
                background: rgba(0,0,0,0.88); border: 1px solid #f59e0b; color: #facc15;
                padding: 6px 18px; border-radius: 6px; font-size: 12px; font-weight: bold;
                pointer-events: none; z-index: 50; text-align: center;
            }}
        </style>
    </head>
    <body>
        <div id="gameContainer">
            <div class="mmorpg-top-hud">
                <div class="player-frame">
                    <div style="font-size: 13px; font-weight: bold; color: #facc15;">🌍 {continente_actual}</div>
                    <div style="font-size: 12px; color: #e2e8f0;">📍 Zona: <b>{zona_actual}</b> | 🐴 {montura_equipada}</div>
                    <div id="coordsText" style="font-size: 11px; color: #94a3b8;">Sector: (600.0 km, 600.0 km) — Escala 1.500.000 km²</div>
                    <div class="hp-bar-bg"><div id="hpFill" class="hp-bar-fill"></div></div>
                    <div id="hpText" style="font-size: 11px; color: #cbd5e1;">HP: 100 / 100</div>
                </div>
                
                <div class="minimap-frame">
                    <canvas id="miniCanvas" width="136" height="136"></canvas>
                </div>
            </div>

            <div id="interactionHint" class="combat-hint">
                ⚔️ <b>WASD / Flechas</b> Mover | <b>1, 2, 3, 4, Q</b> Habilidades Equipadas | <span id="portalMsg" style="color:#38bdf8;">Acércate a la puerta de una ciudad/castillo y pulsa E</span>
            </div>

            <canvas id="gameCanvas"></canvas>

            <div class="mmorpg-action-bar">
                <div class="action-slot" onclick="triggerSkill('1')" title="{s1['nombre']}"><span class="slot-key">1</span>{s1['icono']}<div class="slot-name">{s1['nombre']}</div></div>
                <div class="action-slot" onclick="triggerSkill('2')" title="{s2['nombre']}"><span class="slot-key">2</span>{s2['icono']}<div class="slot-name">{s2['nombre']}</div></div>
                <div class="action-slot" onclick="triggerSkill('3')" title="{s3['nombre']}"><span class="slot-key">3</span>{s3['icono']}<div class="slot-name">{s3['nombre']}</div></div>
                <div class="action-slot" onclick="triggerSkill('4')" title="{s4['nombre']}"><span class="slot-key">4</span>{s4['icono']}<div class="slot-name">{s4['nombre']}</div></div>
                <div class="action-slot" onclick="triggerSkill('q')" title="{sq['nombre']}"><span class="slot-key">Q</span>{sq['icono']}<div class="slot-name">{sq['nombre']}</div></div>
            </div>
        </div>
        
        <script>
            const canvas = document.getElementById("gameCanvas");
            const ctx = canvas.getContext("2d");
            const miniCanvas = document.getElementById("miniCanvas");
            const miniCtx = miniCanvas.getContext("2d");
            const EQUIPPED_SKILLS = {skills_js};

            // Escala masiva del continente activo (120.000 x 120.000 unidades -> 1.500.000 km² globales)
            const WORLD_SIZE = 120000;
            const LAND_MIN = 4000;
            const LAND_MAX = 116000;

            function resizeCanvas() {{
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight * 0.92;
            }}
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();

            let player = {{
                x: 60000, y: 60000, radius: 20, speed: {velocidad_base},
                hp: 100, maxHp: 100, kills: 0,
                shieldActive: false, shieldTimer: 0,
                insideCastle: false, castleName: "",
                cooldowns: {{ '1': 0, '2': 0, '3': 0, '4': 0, 'q': 0 }},
                activeEffects: []
            }};

            let keys = {{}};
            let enemies = [];

            let structures = [
                {{ x: 59300, y: 59150, w: 460, h: 380, name: "Aurelia Capital", type: "city", doorX: 59530, doorY: 59530 }},
                {{ x: 61200, y: 58600, w: 420, h: 360, name: "Castillo de Hojacero", type: "castle", doorX: 61410, doorY: 58960 }},
                {{ x: 58200, y: 60800, w: 380, h: 340, name: "Baluarte Enano de Piedra", type: "castle", doorX: 58390, doorY: 61140 }},
                {{ x: 61600, y: 61100, w: 360, h: 340, name: "Torre de los Arcanos", type: "dungeon", doorX: 61780, doorY: 61440 }}
            ];

            // Entorno alrededor de la región jugable y distribuidor global
            let scenery = [];
            for (let i = 0; i < 450; i++) {{
                let sx = 55000 + Math.random() * 10000;
                let sy = 55000 + Math.random() * 10000;
                let blocked = structures.some(st => sx > st.x - 60 && sx < st.x + st.w + 60 && sy > st.y - 60 && sy < st.y + st.h + 60);
                if (!blocked) {{
                    scenery.push({{
                        x: sx, y: sy,
                        type: Math.random() > 0.45 ? 'tree' : 'rock',
                        radius: 22
                    }});
                }}
            }}

            let templateMobs = {mobs_js};
            for (let i = 0; i < 90; i++) {{
                let tmpl = templateMobs[Math.floor(Math.random() * templateMobs.length)];
                let ex = 55500 + Math.random() * 9000;
                let ey = 55500 + Math.random() * 9000;
                let blocked = structures.some(st => ex > st.x - 40 && ex < st.x + st.w + 40 && ey > st.y - 40 && ey < st.y + st.h + 40);
                if (!blocked) {{
                    enemies.push({{
                        x: ex, y: ey, radius: 18,
                        speed: tmpl.velocidad || 1.8,
                        hp: tmpl.hp, maxHp: tmpl.hp,
                        name: tmpl.nombre, nivel: tmpl.nivel, cooldown: 0
                    }});
                }}
            }}

            window.addEventListener("keydown", (e) => {{
                let k = e.key.toLowerCase();
                keys[k] = true;
                if (['1', '2', '3', '4', 'q'].includes(k)) {{
                    triggerSkill(k);
                }}
                if (k === 'e') {{
                    toggleCastleDoor();
                }}
            }});

            window.addEventListener("keyup", (e) => {{
                let k = e.key.toLowerCase();
                keys[k] = false;
            }});

            function toggleCastleDoor() {{
                if (player.insideCastle) {{
                    player.insideCastle = false;
                    document.getElementById("portalMsg").innerText = "Has salido al mundo exterior.";
                    return;
                }}
                for (let st of structures) {{
                    if (Math.hypot(player.x - st.doorX, player.y - st.doorY) < 75) {{
                        player.insideCastle = true;
                        player.castleName = st.name;
                        document.getElementById("portalMsg").innerText = `🏰 Interior de ${{st.name}} — Pulsa E para salir`;
                        return;
                    }}
                }}
            }}

            function triggerSkill(slotKey) {{
                try {{
                    const skill = EQUIPPED_SKILLS[slotKey];
                    if (!skill) return;
                    if (player.cooldowns[slotKey] > 0) return;

                    player.cooldowns[slotKey] = Number(skill.cooldown) || 30;

                    if (skill.tipo === "defensa" || skill.duracion_escudo > 0) {{
                        player.shieldActive = true;
                        player.shieldTimer = Number(skill.duracion_escudo) || 90;
                    }} else {{
                        const radio = Number(skill.radio) || 100;
                        const dano = Number(skill.dano) || 50;
                        for (let i = enemies.length - 1; i >= 0; i--) {{
                            let en = enemies[i];
                            if (Math.hypot(en.x - player.x, en.y - player.y) <= radio) {{
                                en.hp -= dano;
                                if (en.hp <= 0) {{
                                    enemies.splice(i, 1);
                                    player.kills++;
                                }}
                            }}
                        }}
                    }}

                    player.activeEffects.push({{
                        x: player.x,
                        y: player.y,
                        maxRadius: Number(skill.radio) || 95,
                        color: skill.color || "#facc15",
                        label: `${{skill.icono}} ${{skill.nombre}}`,
                        timer: 22,
                        maxTimer: 22
                    }});
                }} catch (err) {{
                    console.error("Error ejecutando habilidad:", err);
                }}
            }}

            function checkCollision(nx, ny, radius) {{
                if (player.insideCastle) {{
                    let st = structures.find(s => s.name === player.castleName);
                    if (!st) return false;
                    if (nx - radius < st.x + 20 || nx + radius > st.x + st.w - 20 || ny - radius < st.y + 40 || ny + radius > st.y + st.h - 20) {{
                        return Math.hypot(nx - st.doorX, ny - st.doorY) > 55;
                    }}
                    return false;
                }}

                // El océano fuera de LAND_MIN..LAND_MAX bloquea el paso
                if (nx - radius < LAND_MIN || nx + radius > LAND_MAX || ny - radius < LAND_MIN || ny + radius > LAND_MAX) {{
                    return true;
                }}

                for (let st of structures) {{
                    if (nx + radius > st.x && nx - radius < st.x + st.w && ny + radius > st.y && ny - radius < st.y + st.h) {{
                        if (Math.hypot(nx - st.doorX, ny - st.doorY) > 55) return true;
                    }}
                }}

                for (let sc of scenery) {{
                    if (Math.hypot(nx - sc.x, ny - sc.y) < radius + sc.radius * 0.6) return true;
                }}

                return false;
            }}

            function update() {{
                let dx = 0, dy = 0;
                if (keys["arrowup"] || keys["w"]) dy -= player.speed;
                if (keys["arrowdown"] || keys["s"]) dy += player.speed;
                if (keys["arrowleft"] || keys["a"]) dx -= player.speed;
                if (keys["arrowright"] || keys["d"]) dx += player.speed;

                if (!checkCollision(player.x + dx, player.y, player.radius)) player.x += dx;
                if (!checkCollision(player.x, player.y + dy, player.radius)) player.y += dy;

                for (let k in player.cooldowns) {{
                    if (player.cooldowns[k] > 0) player.cooldowns[k]--;
                }}
                if (player.shieldActive) {{
                    player.shieldTimer--;
                    if (player.shieldTimer <= 0) player.shieldActive = false;
                }}

                for (let i = player.activeEffects.length - 1; i >= 0; i--) {{
                    player.activeEffects[i].timer--;
                    if (player.activeEffects[i].timer <= 0) {{
                        player.activeEffects.splice(i, 1);
                    }}
                }}

                let kmX = (player.x / 100).toFixed(1);
                let kmY = (player.y / 100).toFixed(1);
                document.getElementById("coordsText").innerText = `Sector: (${{kmX}} km, ${{kmY}} km) — Continente Activo: 500.000 km²`;

                enemies.forEach(en => {{
                    let edx = player.x - en.x, edy = player.y - en.y;
                    let dist = Math.hypot(edx, edy);
                    if (dist < 380 && dist > 22 && !player.insideCastle) {{
                        let nextX = en.x + (edx / dist) * en.speed;
                        let nextY = en.y + (edy / dist) * en.speed;
                        if (nextX > LAND_MIN + 40 && nextX < LAND_MAX - 40 && nextY > LAND_MIN + 40 && nextY < LAND_MAX - 40) {{
                            en.x = nextX;
                            en.y = nextY;
                        }}
                    }}
                    en.cooldown++;
                    if (dist < 36 && en.cooldown > 45 && !player.insideCastle) {{
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
                ctx.fillStyle = "rgba(0,0,0,0.45)";
                ctx.beginPath(); ctx.ellipse(0, 16, 13, 6, 0, 0, Math.PI * 2); ctx.fill();

                if (player.shieldActive) {{
                    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 4;
                    ctx.fillStyle = "rgba(56, 189, 248, 0.22)";
                    ctx.beginPath(); ctx.arc(0, 0, 32, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
                }}

                ctx.fillStyle = "{color_hex}";
                ctx.fillRect(-12, -10, 24, 24);
                ctx.strokeStyle = "#facc15"; ctx.lineWidth = 2; ctx.strokeRect(-12, -10, 24, 24);

                ctx.fillStyle = "#fde047";
                ctx.beginPath(); ctx.arc(0, -15, 10, 0, Math.PI * 2); ctx.fill();
                ctx.stroke();
                ctx.restore();
            }}

            function drawMonsterSprite(x, y) {{
                ctx.save();
                ctx.translate(x, y);
                ctx.fillStyle = "rgba(0,0,0,0.4)";
                ctx.beginPath(); ctx.ellipse(0, 14, 12, 5, 0, 0, Math.PI * 2); ctx.fill();

                ctx.fillStyle = "#991b1b";
                ctx.fillRect(-14, -14, 28, 28);
                ctx.strokeStyle = "#f87171"; ctx.lineWidth = 2; ctx.strokeRect(-14, -14, 28, 28);
                ctx.fillStyle = "#facc15"; ctx.fillRect(-6, -5, 4, 4); ctx.fillRect(3, -5, 4, 4);
                ctx.restore();
            }}

            function drawCastleExterior(st) {{
                ctx.fillStyle = st.type === 'dungeon' ? "#3f1d1d" : "#475569";
                ctx.fillRect(st.x, st.y, st.w, st.h);
                ctx.strokeStyle = st.type === 'dungeon' ? "#ef4444" : "#f59e0b";
                ctx.lineWidth = 5;
                ctx.strokeRect(st.x, st.y, st.w, st.h);

                ctx.fillStyle = st.type === 'dungeon' ? "#291212" : "#64748b";
                ctx.fillRect(st.x + 28, st.y + 28, st.w - 56, st.h - 56);

                let towers = [
                    [st.x - 14, st.y - 14],
                    [st.x + st.w - 14, st.y - 14],
                    [st.x - 14, st.y + st.h - 14],
                    [st.x + st.w - 14, st.y + st.h - 14]
                ];
                towers.forEach(([tx, ty]) => {{
                    ctx.fillStyle = "#1e293b";
                    ctx.fillRect(tx, ty, 28, 28);
                    ctx.strokeStyle = "#facc15"; ctx.lineWidth = 2;
                    ctx.strokeRect(tx, ty, 28, 28);
                }});

                ctx.fillStyle = "#78350f";
                ctx.fillRect(st.doorX - 24, st.doorY - 14, 48, 28);
                ctx.strokeStyle = "#facc15"; ctx.lineWidth = 2;
                ctx.strokeRect(st.doorX - 24, st.doorY - 14, 48, 28);

                ctx.fillStyle = "rgba(15, 23, 42, 0.92)";
                ctx.fillRect(st.x + st.w/2 - 135, st.y - 36, 270, 26);
                ctx.fillStyle = "#facc15"; ctx.font = "bold 13px sans-serif"; ctx.textAlign = "center";
                ctx.fillText(st.name + " [Pulsa E en Puerta]", st.x + st.w/2, st.y - 18);
            }}

            function draw() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.save();

                let camX = canvas.width / 2 - player.x;
                let camY = canvas.height / 2 - player.y;
                ctx.translate(camX, camY);

                if (player.insideCastle) {{
                    ctx.fillStyle = "#1e293b"; ctx.fillRect(player.x - 650, player.y - 650, 1300, 1300);
                    ctx.strokeStyle = "#d97706"; ctx.lineWidth = 8; ctx.strokeRect(player.x - 550, player.y - 550, 1100, 1100);
                    ctx.fillStyle = "#facc15"; ctx.font = "bold 24px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(`🏰 Interior de ${{player.castleName}}`, player.x, player.y - 200);
                    ctx.font = "bold 14px sans-serif";
                    ctx.fillText("Salón del Trono, Gremio y Comercio Real — Pulsa E para salir", player.x, player.y - 160);
                    drawPlayerSprite(player.x, player.y);
                    ctx.restore();
                    return;
                }}

                // Océano exterior (bloqueado)
                ctx.fillStyle = "#0284c7"; ctx.fillRect(0, 0, WORLD_SIZE, WORLD_SIZE);
                // Costa de arena
                ctx.fillStyle = "#d97706"; ctx.fillRect(LAND_MIN - 200, LAND_MIN - 200, (LAND_MAX - LAND_MIN) + 400, (LAND_MAX - LAND_MIN) + 400);
                // Masa continental de tierra firme
                ctx.fillStyle = "#15803d"; ctx.fillRect(LAND_MIN, LAND_MIN, LAND_MAX - LAND_MIN, LAND_MAX - LAND_MIN);

                // Calzadas reales conectando ciudades
                ctx.strokeStyle = "#92400e"; ctx.lineWidth = 28;
                ctx.beginPath();
                ctx.moveTo(59530, 59530);
                ctx.lineTo(61410, 58960);
                ctx.moveTo(59530, 59530);
                ctx.lineTo(58390, 61140);
                ctx.moveTo(59530, 59530);
                ctx.lineTo(61780, 61440);
                ctx.stroke();

                structures.forEach(st => drawCastleExterior(st));

                scenery.forEach(sc => {{
                    if (Math.abs(sc.x - player.x) > 1400 || Math.abs(sc.y - player.y) > 1000) return;
                    if (sc.type === 'tree') {{
                        ctx.fillStyle = "#14532d"; ctx.beginPath(); ctx.arc(sc.x, sc.y - 8, sc.radius, 0, Math.PI*2); ctx.fill();
                    }} else {{
                        ctx.fillStyle = "#475569"; ctx.fillRect(sc.x - sc.radius, sc.y - sc.radius*0.7, sc.radius*2, sc.radius*1.4);
                    }}
                }});

                enemies.forEach(en => {{
                    if (Math.abs(en.x - player.x) > 1400 || Math.abs(en.y - player.y) > 1000) return;
                    drawMonsterSprite(en.x, en.y);
                    ctx.fillStyle = "#000"; ctx.fillRect(en.x - 20, en.y - 28, 40, 6);
                    ctx.fillStyle = "#22c55e"; ctx.fillRect(en.x - 19, en.y - 27, 38 * (en.hp / en.maxHp), 4);
                    ctx.fillStyle = "#f87171"; ctx.font = "bold 11px sans-serif"; ctx.textAlign = "center";
                    ctx.fillText(en.name + ` [${{en.nivel}}]`, en.x, en.y - 34);
                }});

                // Efectos visuales de habilidades equipadas
                player.activeEffects.forEach(ef => {{
                    let progress = 1 - (ef.timer / ef.maxTimer);
                    let r = Math.max(15, ef.maxRadius * progress);
                    ctx.strokeStyle = ef.color;
                    ctx.lineWidth = 4;
                    ctx.beginPath(); ctx.arc(ef.x, ef.y, r, 0, Math.PI * 2); ctx.stroke();
                    ctx.fillStyle = ef.color;
                    ctx.font = "bold 12px sans-serif";
                    ctx.textAlign = "center";
                    ctx.fillText(ef.label, ef.x, ef.y - 42 - (progress * 18));
                }});

                drawPlayerSprite(player.x, player.y);
                ctx.fillStyle = "#facc15"; ctx.font = "bold 13px sans-serif"; ctx.textAlign = "center";
                ctx.fillText("⭐ Tu Héroe (Kills: " + player.kills + ")", player.x, player.y - 30);

                ctx.restore();

                // Minimapa global
                miniCtx.clearRect(0, 0, 136, 136);
                miniCtx.fillStyle = "#0284c7"; miniCtx.fillRect(0, 0, 136, 136);
                miniCtx.fillStyle = "#15803d"; miniCtx.fillRect(6, 6, 124, 124);
                let mX = (player.x / WORLD_SIZE) * 136, mY = (player.y / WORLD_SIZE) * 136;
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