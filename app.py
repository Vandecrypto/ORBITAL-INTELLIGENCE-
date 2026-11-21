import streamlit as st
import streamlit.components.v1 as components
import base64
from physics import (
    orbital_radius,
    circular_orbital_velocity,
    orbital_period
)
# LOAD SATELLITE MODULE

with open("satellites.js", "r", encoding="utf-8") as file:
    satellite_js = file.read()

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ORBITAL INTELLIGENCE 2.0",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# LOAD SPACE BACKGROUND
# 

# ==========================================
# MAIN INTERFACE DESIGN
# ==========================================

st.markdown(f"""
<style>

.stApp {{

    background-image:
    url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;

}}

header {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

.block-container {{
    padding-top: 1rem;
    padding-bottom: 0rem;
}}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PROJECT TITLE
# ==========================================

st.markdown("""
<h1 style="
text-align:center;
color:#66D9FF;
letter-spacing:5px;
font-size:34px;
">
ORBITAL INTELLIGENCE 2.0
</h1>

<p style="
text-align:center;
color:#A8DFFF;
letter-spacing:3px;
font-size:12px;
">
SPACE TRAFFIC MANAGEMENT & ORBITAL SUSTAINABILITY
</p>
""", unsafe_allow_html=True)


# ==========================================
# 3D EARTH ENVIRONMENT
# ==========================================

earth_html = r"""

<!DOCTYPE html>

<html>

<head>

<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js">
</script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js">
</script>
<style>

body {
    margin: 0;
    overflow: hidden;
    background: transparent;
}

canvas {
    display: block;
}

</style>

</head>

<body>

<script>

// =================================
// SCENE
// =================================

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(
    45,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);

camera.position.z = 20;


// =================================
// RENDERER
// =================================

const renderer = new THREE.WebGLRenderer({
    antialias: true,
    alpha: true
});

renderer.setSize(
    window.innerWidth,
    window.innerHeight
);

renderer.setPixelRatio(
    Math.min(window.devicePixelRatio, 2)
);

document.body.appendChild(renderer.domElement);
// =================================
// INTERACTIVE CAMERA CONTROLS
// =================================

const controls = new THREE.OrbitControls(
    camera,
    renderer.domElement
);

controls.enableDamping = true;
controls.dampingFactor = 0.05;

controls.enableZoom = true;
controls.zoomSpeed = 1.0;

controls.enablePan = true;
controls.panSpeed = 0.8;

controls.minDistance = 2.2;
controls.maxDistance = 25;

controls.target.set(0, 0, 0);
// =================================
// CAMERA CONTROL PANEL
// =================================

const cameraPanel = document.createElement("div");

cameraPanel.style.position = "absolute";
cameraPanel.style.top = "15px";
cameraPanel.style.right = "15px";
cameraPanel.style.zIndex = "100";
cameraPanel.style.display = "flex";
cameraPanel.style.flexDirection = "column";
cameraPanel.style.gap = "8px";

cameraPanel.innerHTML = `
    <button id="zoomIn">＋ Zoom In</button>
    <button id="zoomOut">－ Zoom Out</button>
    <button id="resetCamera">⟲ Reset View</button>
    <button id="earthFocus">🌍 Earth Focus</button>
`;

document.body.appendChild(cameraPanel);


// Button styling

cameraPanel.querySelectorAll("button").forEach(button => {

    button.style.padding = "10px 14px";
    button.style.background = "rgba(0, 25, 55, 0.9)";
    button.style.color = "#66D9FF";
    button.style.border = "1px solid #168BFF";
    button.style.borderRadius = "8px";
    button.style.cursor = "pointer";
    button.style.fontSize = "13px";

});


// Zoom In

document.getElementById("zoomIn").addEventListener("click", () => {

    controls.dollyIn(1.2);
    controls.update();

});


// Zoom Out

document.getElementById("zoomOut").addEventListener("click", () => {

    controls.dollyOut(1.2);
    controls.update();

});


// Reset Camera

document.getElementById("resetCamera").addEventListener("click", () => {

    camera.position.set(0, 0, 20);
    controls.target.set(0, 0, 0);
    controls.update();

});


// Earth Focus

document.getElementById("earthFocus").addEventListener("click", () => {

    controls.target.set(0, 0, 0);
    controls.update();

});

// =================================
// LIGHTING
// =================================

const ambientLight = new THREE.AmbientLight(
    0xffffff,
    0.8
);

scene.add(ambientLight);

const sunlight = new THREE.DirectionalLight(
    0xffffff,
    2
);

sunlight.position.set(5, 3, 5);

scene.add(sunlight);


// =================================
// EARTH
// =================================

const earthGeometry = new THREE.SphereGeometry(
    1,
    96,
    96
);

const textureLoader = new THREE.TextureLoader();

const earthTexture = textureLoader.load(
    "https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg"
);

const earthMaterial = new THREE.MeshPhongMaterial({

    map: earthTexture,

    shininess: 15

});

const earth = new THREE.Mesh(
    earthGeometry,
    earthMaterial
);

scene.add(earth);


// =================================
// BLUE ATMOSPHERE
// =================================

const atmosphereGeometry = new THREE.SphereGeometry(
    1.035,
    96,
    96
);

const atmosphereMaterial = new THREE.MeshBasicMaterial({

    color: 0x168bff,

    transparent: true,

    opacity: 0.12,

    side: THREE.BackSide

});

const atmosphere = new THREE.Mesh(
    atmosphereGeometry,
    atmosphereMaterial

);

scene.add(atmosphere);
// =================================
// PHYSICS-BASED ORBITAL ENVIRONMENT
// =================================

// Earth radius in metres
const EARTH_RADIUS_M = 6371000;

// Convert altitude into visual orbital radius
function getOrbitalRadius(altitudeKm) {

    const altitudeM = altitudeKm * 1000;

    return (EARTH_RADIUS_M + altitudeM) / EARTH_RADIUS_M;

}


// Create an orbital path using actual altitude
function createOrbit(altitudeKm, color, inclination) {

    const radius = getOrbitalRadius(altitudeKm);

    const geometry = new THREE.TorusGeometry(
        radius,
        0.003,
        8,
        300
    );

    const material = new THREE.MeshBasicMaterial({

        color: color,

        transparent: true,

        opacity: 0.8

    });

    const orbit = new THREE.Mesh(
        geometry,
        material
    );

    // Inclination in degrees
    orbit.rotation.x = inclination * Math.PI / 180;

    scene.add(orbit);

    return orbit;

}


// =================================
// ORBITAL REGIMES
// =================================

// Low Earth Orbit
const orbit1 = createOrbit(
    550,
    0x00ccff,
    0
);


// Polar Low Earth Orbit
const orbit2 = createOrbit(
    800,
    0x00ff99,
    90
);


// Medium Earth Orbit
const orbit3 = createOrbit(
    20200,
    0xffcc00,
    55
);


// Geostationary Orbit
const orbit4 = createOrbit(
      35786,
    0xff6600,
    0
);



// =================================
// ANIMATION
// =================================
// =================================
// ANIMATION ENGINE
// =================================

function animate() {

    requestAnimationFrame(animate);

    // Smooth camera controls
    controls.update();

    // Slow Earth rotation
    earth.rotation.y += 0.0005;

    

    // Render 3D environment
    renderer.render(scene, camera);

}

animate();

// =================================
// RESPONSIVE SCREEN
// =================================

window.addEventListener("resize", () => {

    camera.aspect =
        window.innerWidth / window.innerHeight;

    camera.updateProjectionMatrix();

    renderer.setSize(
        window.innerWidth,
        window.innerHeight
    );

});

</script>

</body>

</html>

"""



# ==========================================
# DISPLAY 3D EARTH
# ==========================================

components.html(
    earth_html,
    height=680,
    scrolling=False
)


# ==========================================
# MISSION STATUS
# ==========================================

st.markdown("""
<div style="
text-align:center;
color:#65D9FF;
font-size:13px;
letter-spacing:3px;
">
● MISSION CONTROL INITIALISED
</div>
""", unsafe_allow_html=True)
# ==========================================
# SCIENTIFIC COMPUTATION CENTRE
# ==========================================

st.markdown("---")

st.header("SCIENTIFIC COMPUTATION CENTRE")

altitude = st.number_input(
    "Satellite Altitude (km)",
    min_value=160.0,
    max_value=100000.0,
    value=400.0,
    step=10.0
)

# Perform actual calculations

radius = orbital_radius(altitude)

velocity = circular_orbital_velocity(altitude)

period = orbital_period(altitude)

st.subheader("Orbital Mechanics Analysis")

st.latex(r"v = \sqrt{\frac{\mu}{r}}")

st.write("Circular Orbital Velocity")

st.success(f"{velocity / 1000:.4f} km/s")

st.latex(r"T = 2\pi\sqrt{\frac{r^3}{\mu}}")

st.write("Orbital Period")

st.success(f"{period / 60:.2f} minutes")

st.write("Orbital Radius")

st.info(f"{radius / 1000:.2f} km")

st.caption(
    "Model: Newtonian Two-Body Circular Orbit"
)
