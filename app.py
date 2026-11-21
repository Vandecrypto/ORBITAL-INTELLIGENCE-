import streamlit as st
import streamlit.components.v1 as components
import base64
from physics import (
    orbital_radius,
    circular_orbital_velocity,
    orbital_period
)

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

camera.position.z = 3.5;


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
// MOUSE ROTATION
// =================================

let dragging = false;

let previousX = 0;

let previousY = 0;

let rotationSpeed = 0.002;

document.addEventListener("pointerdown", (event) => {

    dragging = true;

    previousX = event.clientX;

    previousY = event.clientY;

});

document.addEventListener("pointerup", () => {

    dragging = false;

});

document.addEventListener("pointermove", (event) => {

    if (!dragging) return;

    const movementX = event.clientX - previousX;

    const movementY = event.clientY - previousY;

    earth.rotation.y += movementX * 0.005;

    earth.rotation.x += movementY * 0.005;

    previousX = event.clientX;

    previousY = event.clientY;

});


// =================================
// ZOOM
// =================================

document.addEventListener("wheel", (event) => {

    camera.position.z += event.deltaY * 0.002;

    camera.position.z = Math.max(
        2,
        Math.min(6, camera.position.z)
    );

});


// =================================
// ANIMATION
// =================================

function animate() {

    requestAnimationFrame(animate);

    if (!dragging) {

        earth.rotation.y += rotationSpeed;

    }

    orbit1.rotation.z += 0.0003;

    orbit2.rotation.z -= 0.0002;

    orbit3.rotation.z += 0.00015;

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
