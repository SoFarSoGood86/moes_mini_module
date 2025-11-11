<img width="1463" height="366" alt="MOES_HA_HACS" src="https://github.com/user-attachments/assets/d049a712-5e15-422d-8f18-a6926ce2339f" />


# MOES Mini Module Intelligent (local)

[![HACS Custom](https://img.shields.io/badge/HACS-Custom-blue.svg?logo=homeassistant)](https://hacs.xyz)
[![GitHub Release](https://img.shields.io/github/v/release/SoFarSoGood86/moes_mini_module)](https://github.com/SoFarSoGood86/moes_mini_module/releases)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2025.1+-blue.svg)

## Description
Cette intégration Home Assistant permet le contrôle en local (TuyaLan Protocol) sans passer par le cloud.
Elle regroupe les modules connectés "MOES Mini" (dimmer, switch, curtain, garage) via la bibliothèque [`tinytuya`](https://github.com/jasonacox/tinytuya) dans une intégration unique pour une installation domotique simplifiée.

## Modules supportés
- MOES - Mini Dimmer module 1 gang (dimmer_1)
- MOES - Mini Dimmer module 2 gang (dimmer_2)
- MOES - Mini Switch module 1 gang (switch_1)
- MOES - Mini Switch module 2 gang (switch_2)
- MOES - Mini Switch module 3 gang (switch_3)
- MOES - Mini Switch module 4 gang (switch_4)
- MOES - Mini Smart Curtain Switch module (curtain)
- MOES - Mini Smart Garage Door module (garage)

## Fonctionnalités
- Contrôle local LAN (pas de cloud nécessaire)
- Lights: on/off + brightness (dimmers)
- Switches: 1..4 canaux on/off
- Covers: open/close/stop + position

## Prérequis
- Home Assistant 2021.12 ou supérieur
- Python 3.11+
- [`tinytuya==1.17.4`](https://github.com/jasonacox/tinytuya).
- Adresse IP, device_id et local_key pour chaque module

## Installation via HACS
1. Ajouter le dépôt comme dépôt personnalisé dans HACS (type: Intégration).

   [![Set up a new integration in Home Assistant](https://my.home-assistant.io/badges/config_flow_start.svg)](https://github.com/SoFarSoGood86/moes_mini_module)
3. Installer l'intégration depuis HACS et redémarrer Home Assistant.
4. Ajouter l'intégration via **Paramètres → Appareils et Services → Ajouter une intégration → MOES Mini Module Intelligent (local)**.
5. Saisir l'IP, le `device_id`, le `local_key` et sélectionner le `device_type`.

## Configuration

Vous pouvez configurer vos modules soit :
- via **l’interface Home Assistant** (ajout d’intégration),
- soit manuellement en **YAML**.

## Exemple de configuration YAML :

```yaml
moes_mini_module:
  devices:
    - name: "Variateur salon"
      ip: 192.168.1.42
      local_key: a1b2c3d4e5f6g7h8
      device_id: 1234567890abcdef1234abcd
      type: dimmer_1gang

    - name: "Interrupteur cuisine"
      ip: 192.168.1.43
      local_key: z9y8x7w6v5u4t3s2
      device_id: 0987654321abcdefabcd4321
      type: switch_2gang
```

Ou, copier `custom_components/moes_mini_module` dans `config/custom_components/` et redémarrer HA.

## Exemple YAML
Voir `example_config.yaml` fourni.

## Comment obtenir la “Local Key” Tuya

Les modules MOES (comme la plupart des appareils Tuya) nécessitent une **clé locale** pour permettre la communication locale chiffrée.

### Scanner réseau :
TinyTuya intègre un scanner réseau permettant de localiser les appareils Tuya sur votre réseau local. Il affiche l'adresse, l'identifiant et la version de chaque appareil. 
Votre réseau local et votre pare-feu doivent autoriser le trafic UDP (ports 6666, 6667 et 7000) et TCP (port 6668).
Ouvrez le terminal de Homme Assistant et entrez la commande suivante :

```bash
python -m tinytuya scan
```
### Étape 1 – Créer un compte développeur Tuya
1. Rendez-vous sur [https://iot.tuya.com](https://iot.tuya.com)
2. Créez un compte gratuit.
3. Créez un **Cloud Project** (type “Smart Home”).

### Étape 2 – Lier votre compte Tuya Smart / Smart Life
1. Dans votre projet, allez dans **“Link devices by App Account”**
2. Cliquez sur **“Add App Account”**
3. Scannez le QR code depuis l’application mobile Tuya Smart (ou Smart Life).
4. Vos appareils seront automatiquement visibles dans la console.

### Étape 3 – Récupérer la clé locale
1. Sélectionnez votre module dans la liste.
2. Cliquez sur **Device Information**
3. Notez :
   - `Device ID`
   - `Local Key`
   - `IP Address`

### Étape 4 – Insérez la clé dans votre configuration Home Assistant
Exemple :
```yaml
local_key: a1b2c3d4e5f6g7h8
```
## Tests & CI

Ce projet inclut :
- **Pytest** pour les tests unitaires (`tests/`)
- **Linting** (`flake8`)
- **Hassfest** pour la conformité Home Assistant
- **GitHub Actions CI**

Exécuter les tests localement :
```bash
pytest
```

## Mappings DP courants (à vérifier selon firmware)
- Dimmer: `DP 1` = ON/OFF, `DP 2` = Brightness (0–100)
- Switch multi-gang: `DP 1..4` = on/off pour chaque canal
- Curtain/Garage: `DP 1` = open, `DP 2` = close, `DP 3` = stop, `DP 101` = position (0–100)

## Limitations
- Les `dps` peuvent varier selon firmware. Si un appareil ne répond pas comme prévu, récupérez le `status()` via tinytuya et ouvrez une issue.
- L'intégration nécessite la `local_key` pour le contrôle local.

## Structure du dépôt

```
custom_components/moes_mini_module/
├── __init__.py
├── manifest.json
├── config_flow.py
├── switch.py
├── light.py
├── cover.py
├── services.yaml
├── translations/
│   └── fr.json
└── icon.png
```

## Changelog (extrait)
- v1.1.0 : Ajout détection DPS, options DP, tests, CI, icon, example_config.yaml

## Historique des versions

| Version | Date | Changements |
|----------|------|--------------|
- v1.1.0 | 2025-11-10 | Ajout complet des modules Dimmer, Switch, Curtain, Garage + gestion YAML + CI |
- v1.0.0 | 2025-11-09 | Première version fonctionnelle |

## Aide / Issues
Ouvrez une issue sur le dépôt GitHub : `https://github.com/SoFarSoGood86/moes_mini_module/issues`

## Support

Si vous aimez cette intégration, vous pouvez m’offrir un café ☕️ :

[![Buy Me A Coffee](https://github.com/user-attachments/assets/5b064037-c6d4-4d66-b53a-21e340178782 )](https://www.buymeacoffee.com/SoFarSoGood86)








