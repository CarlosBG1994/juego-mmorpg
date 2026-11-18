<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Snd-Worlds - Editor de Mapas y Mundos MMORPG</title>
    <style>
        body { margin: 0; background-color: #0b1017; color: #fff; font-family: 'Segoe UI', Tahoma, sans-serif; overflow: hidden; display: flex; height: 100vh; }
        #sidebar { width: 320px; background: rgba(15, 23, 42, 0.95); border-right: 2px solid #b45309; padding: 20px; display: flex; flex-direction: column; gap: 15px; z-index: 10; box-shadow: 4px 0 20px rgba(0,0,0,0.8); overflow-y: auto; }
        h1 { font-size: 18px; color: #facc15; margin: 0 0 10px 0; border-bottom: 2px solid #b45309; padding-bottom: 8px; }
        .tool-group { display: flex; flex-direction: column; gap: 8px; }
        label { font-size: 13px; color: #cbd5e1; font-weight: bold; }
        select, button { background: #1e293b; color: #fff; border: 1px solid #475569; padding: 10px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: bold; transition: all 0.2s; }
        button:hover { background: #b45309; border-color: #f59e0b; }
        .btn-action { background: #047857; border-color: #059669; }
        .btn-action:hover { background: #059669; }
        #canvasContainer { flex-grow: 1; position: relative; background: #0284c7; overflow: hidden; }
        canvas { display: block; cursor: crosshair; }
        .coords-hud { position: absolute; bottom: 15px; left: 15px; background: rgba(15, 23, 42, 0.9); border: 1px solid #b45309; padding: 8px 15px; border-radius: 6px; font-family: monospace; font-size: 13px; color: #facc15; pointer-events: none; }
    </style>
</head>
<body>

    <div id="sidebar">
        <h1>🗺️ Editor de Mundos Snd-Worlds</h1>
        
        <div class="tool-group">
            <label>Herramienta / Objeto a Pintar:</label>
            <select id="toolSelect">
                <option value="continent">🟢 Continente / Tierra Firme</option>
                <option value="archipelago">🏝️ Archipiélago / Isla Navegable</option>
                <option value="city">🏛️ Ciudad / Capital (Valoria)</option>
                <option value="castle">🏰 Castillo / Fortaleza</option>
                <option value="dungeon">🕳️ Entrada de Mazmorra</option>
                <option value="tree">🌲 Bosque / Árboles</option>
                <option value="rock">🪨 Cantera / Rocas</option>
                <option value="npc_plebeian">💬 Plebeyo Callejero</option>
                <option value="npc_mythic">⭐ NPC Ermitaño (Misión Mítica)</option>
                <option value="mob">👹 Mob / Monstruo</option>
                <option value="eraser">🧹 Borrar Elemento</option>
            </select>
        </div>

        <div class="tool-group">
            <label>Zona de Destino / Escala:</label>
            <select id="zoneSelect">
                <option value="Continente I">Continente I (Niveles 1-100)</option>
                <option value="Continente II">Continente II (Raid & Mazmorras)</option>
                <option value="Oceano Abierto">Océano y Archipiélagos</option>
            </select>
        </div>

        <div class="tool-group">
            <label>Acciones de Mapa:</label>
            <button class="btn-action" onclick="exportMapData()">💾 Exportar Mapa (JSON)</button>
            <button onclick="clearMap()">🗑️ Limpiar Todo</button>
        </div>

        <div style="font-size: 11px; color: #94a3b8; line-height: 1.4; margin-top: auto;">
            <b>Instrucciones:</b> Selecciona una herramienta, haz clic en el mapa para colocar estructuras, NPCs o monstruos en el mundo abierto de 1.5M km². Usa W, A, S, D o arrastra para moverte.
        </div>
    </div>

    <div id="canvasContainer">
        <canvas id="editorCanvas"></canvas>
        <div id="coordsHUD" class="coords-hud">X: 3000 | Y: 3000 | Zoom: 1.0x</div>
    </div>

    <script>
        const canvas = document.getElementById("editorCanvas");
        const ctx = canvas.getContext("2d");
        const coordsHUD = document.getElementById("coordsHUD");

        function resizeCanvas() {
            canvas.width = document.getElementById("canvasContainer").clientWidth;
            canvas.height = document.getElementById("canvasContainer").clientHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        let camera = { x: 3000, y: 3000, zoom: 1.0 };
        let isDragging = false;
        let startX, startY;

        // Elementos editables del mundo
        let worldEntities = [
            { x: 2600, y: 2600, type: "continent", name: "Valoria Central" },
            { x: 1200, y: 1200, type: "archipelago", name: "Archipiélago Norte" },
            { x: 4500, y: 1200, type: "archipelago", name: "Islas Brumas" },
            { x: 2300, y: 2300, type: "city", name: "Aurelia Capital" },
            { x: 1200, y: 1200, type: "npc_mythic", name: "Maestro Ignis (Ermitaño)" }
        ];

        window.addEventListener("mousedown", (e) => {
            if (e.button === 1 || e.shiftKey) { // Botón central o Shift + Clic para mover cámara
                isDragging = true;
                startX = e.clientX;
                startY = e.clientY;
            } else if (e.button === 0) { // Clic izquierdo para pintar
                let rect = canvas.getBoundingClientRect();
                let mouseX = (e.clientX - rect.left - canvas.width / 2) / camera.zoom + camera.x;
                let mouseY = (e.clientY - rect.top - canvas.height / 2) / camera.zoom + camera.y;
                
                let selectedTool = document.getElementById("toolSelect").value;
                if (selectedTool === "eraser") {
                    worldEntities = worldEntities.filter(en => Math.hypot(en.x - mouseX, en.y - mouseY) > 30);
                } else {
                    worldEntities.push({ x: mouseX, y: mouseY, type: selectedTool, name: selectedTool.toUpperCase() });
                }
            }
        });

        window.addEventListener("mousemove", (e) => {
            let rect = canvas.getBoundingClientRect();
            let mouseX = Math.round((e.clientX - rect.left - canvas.width / 2) / camera.zoom + camera.x);
            let mouseY = Math.round((e.clientY - rect.top - canvas.height / 2) / camera.zoom + camera.y);
            coordsHUD.innerText = `X: ${mouseX} | Y: ${mouseY} | Zoom: ${camera.zoom.toFixed(1)}x`;

            if (isDragging) {
                camera.x -= (e.clientX - startX) / camera.zoom;
                camera.y -= (e.clientY - startY) / camera.zoom;
                startX = e.clientX;
                startY = e.clientY;
            }
        });

        window.addEventListener("mouseup", () => isDragging = false);
        window.addEventListener("wheel", (e) => {
            e.preventDefault();
            if (e.deltaY < 0) camera.zoom = Math.min(camera.zoom * 1.1, 2.5);
            else camera.zoom = Math.max(camera.zoom / 1.1, 0.4);
        }, { passive: false });

        function drawWorld() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.save();
            
            ctx.translate(canvas.width / 2, canvas.height / 2);
            ctx.scale(camera.zoom, camera.zoom);
            ctx.translate(-camera.x, -camera.y);

            // 1. Océano infinito de fondo
            ctx.fillStyle = "#0284c7";
            ctx.fillRect(0, 0, 6000, 6000);

            // 2. Dibujar Entidades del Mapa
            worldEntities.forEach(en => {
                ctx.save();
                ctx.translate(en.x, en.y);
                if (en.type === 'continent') {
                    ctx.fillStyle = "#1a2e12"; ctx.fillRect(-400, -400, 800, 800);
                    ctx.strokeStyle = "#f59e0b"; ctx.lineWidth = 4; ctx.strokeRect(-400, -400, 800, 800);
                } else if (en.type === 'archipelago') {
                    ctx.fillStyle = "#15803d"; ctx.fillRect(-180, -180, 360, 360);
                    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3; ctx.strokeRect(-180, -180, 360, 360);
                } else if (en.type === 'city') {
                    ctx.fillStyle = "#334155"; ctx.fillRect(-90, -70, 180, 140);
                    ctx.strokeStyle = "#eab308"; ctx.lineWidth = 3; ctx.strokeRect(-90, -70, 180, 140);
                } else if (en.type === 'npc_mythic') {
                    ctx.fillStyle = "#9333ea"; ctx.beginPath(); ctx.arc(0, 0, 16, 0, Math.PI*2); ctx.fill();
                } else if (en.type === 'mob') {
                    ctx.fillStyle = "#dc2626"; ctx.beginPath(); ctx.arc(0, 0, 14, 0, Math.PI*2); ctx.fill();
                } else {
                    ctx.fillStyle = "#475569"; ctx.beginPath(); ctx.arc(0, 0, 12, 0, Math.PI*2); ctx.fill();
                }
                
                ctx.fillStyle = "#fff"; ctx.font = "bold 12px sans-serif"; ctx.textAlign = "center";
                ctx.fillText(en.name, 0, -22);
                ctx.restore();
            });

            ctx.restore();
            requestAnimationFrame(drawWorld);
        }

        function exportMapData() {
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(worldEntities, null, 4));
            const downloadAnchor = document.createElement('a');
            downloadAnchor.setAttribute("href", dataStr);
            downloadAnchor.setAttribute("download", "snd_worlds_map_data.json");
            document.body.appendChild(downloadAnchor);
            downloadAnchor.click();
            downloadAnchor.remove();
        }

        function clearMap() {
            if (confirm("¿Estás seguro de borrar todos los elementos del mapa?")) {
                worldEntities = [];
            }
        }

        drawWorld();
    </script>
</body>
</html>