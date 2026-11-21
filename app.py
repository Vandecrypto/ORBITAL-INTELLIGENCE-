I import streamlit as st
import streamlit.components.v1 as components
import base64

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
// ORBITAL RINGS
// =================================

function createOrbit(radius, color, rotationX, rotationY) {

    const geometry = new THREE.TorusGeometry(
        radius,
        0.002,
        8,
        200
    );

    const material = new THREE.MeshBasicMaterial({

        color: color,

        transparent: true,

        opacity: 0.65

    });

    const orbit = new THREE.Mesh(
        geometry,
        material
    );

    orbit.rotation.x = rotationX;

    orbit.rotation.y = rotationY;

    scene.add(orbit);

    return orbit;

}

const orbit1 = createOrbit(
    1.35,
    0x00aaff,
    1.1,
    0.2
);

const orbit2 = createOrbit(
    1.55,
    0x0077ff,
    0.5,
    1.0
);

const orbit3 = createOrbit(
    1.75,
    0x33ccff,
    1.4,
    0.8
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
