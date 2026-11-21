// ==========================================
// ORBITAL INTELLIGENCE 2.0
// SATELLITE 3D MODEL ENGINE
// ==========================================

function createSatellite(scene, position = { x: 0, y: 0, z: 0 }) {

    const satellite = new THREE.Group();

    // ======================================
    // CENTRAL SPACECRAFT BODY
    // ======================================

    const bodyGeometry = new THREE.BoxGeometry(
        0.16,
        0.20,
        0.16
    );

    const bodyMaterial = new THREE.MeshStandardMaterial({
        color: 0xb5b5b5,
        metalness: 0.85,
        roughness: 0.35
    });

    const body = new THREE.Mesh(
        bodyGeometry,
        bodyMaterial
    );

    satellite.add(body);


    // ======================================
    // SOLAR PANEL MATERIAL
    // ======================================

    const panelMaterial = new THREE.MeshStandardMaterial({
        color: 0x123b83,
        metalness: 0.55,
        roughness: 0.3
    });


    // ======================================
    // SOLAR PANEL FUNCTION
    // ======================================

    function createSolarPanel(xPosition) {

        const panelGroup = new THREE.Group();

        const panelGeometry = new THREE.BoxGeometry(
            0.55,
            0.025,
            0.30
        );

        const panel = new THREE.Mesh(
            panelGeometry,
            panelMaterial
        );

        panelGroup.add(panel);

        panelGroup.position.x = xPosition;

        satellite.add(panelGroup);

    }


    // Left Solar Panel
    createSolarPanel(-0.40);

    // Right Solar Panel
    createSolarPanel(0.40);


    // ======================================
    // ANTENNA SUPPORT
    // ======================================

    const antennaGeometry = new THREE.CylinderGeometry(
        0.012,
        0.012,
        0.22,
        12
    );

    const antennaMaterial = new THREE.MeshStandardMaterial({
        color: 0xcccccc,
        metalness: 0.9,
        roughness: 0.25
    });

    const antenna = new THREE.Mesh(
        antennaGeometry,
        antennaMaterial
    );

    antenna.position.y = 0.20;

    satellite.add(antenna);


    // ======================================
    // ANTENNA DISH
    // ======================================

    const dishGeometry = new THREE.SphereGeometry(
        0.12,
        24,
        16,
        0,
        Math.PI * 2,
        0,
        Math.PI / 2
    );

    const dishMaterial = new THREE.MeshStandardMaterial({
        color: 0xd6d6d6,
        metalness: 0.8,
        roughness: 0.25,
        side: THREE.DoubleSide
    });

    const dish = new THREE.Mesh(
        dishGeometry,
        dishMaterial
    );

    dish.rotation.x = Math.PI;

    dish.position.y = 0.32;

    satellite.add(dish);


    // ======================================
    // POSITION
    // ======================================

    satellite.position.set(
        position.x,
        position.y,
        position.z
    );


    // Add satellite to scene
    scene.add(satellite);

    return satellite;

                                            }
