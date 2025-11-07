# MOES Mini Module Intelligent (local)

## Description
Cette intégration Home Assistant permet le contrôle local (LAN) des modules MOES Mini Joli Intelligent (dimmer, switch, curtain, garage) via la bibliothèque `tinytuya`.
Elle regroupe plusieurs types d'appareils dans une intégration unique pour une maintenance simplifiée.

## Modules supportés
- MOES Mini Joli Intelligent 1 gang Dimmer (dimmer_1)
- MOES Mini Joli Intelligent 2 gang Dimmer (dimmer_2)
- MOES Mini Joli Intelligent 1 gang Switch (switch_1)
- MOES Mini Joli Intelligent 2 gang Switch (switch_2)
- MOES Mini Joli Intelligent 3 gang Switch (switch_3)
- MOES Mini Joli Intelligent 4 gang Switch (switch_4)
- MOES Mini smart curtain switch module (curtain)
- MOES Mini smart garage door module (garage)

## Fonctionnalités
- Contrôle local LAN (pas de cloud nécessaire)
- Lights: on/off + brightness (dimmers)
- Switches: 1..4 canaux on/off
- Covers: open/close/stop + position

## Prérequis
- Home Assistant 2021.12 ou supérieur
- Python 3.11+
- `tinytuya==1.17.4`
- Adresse IP, device_id et local_key pour chaque module

## Installation via HACS
1. Ajouter le dépôt `https://github.com/SoFarSoGood86/moes_mini_module` comme dépôt personnalisé dans HACS (type: Intégration).
2. Installer l'intégration depuis HACS et redémarrer Home Assistant.
3. Ajouter l'intégration via **Paramètres → Appareils et Services → Ajouter une intégration → MOES Mini Module Intelligent (local)**.
4. Saisir l'IP, le `device_id`, le `local_key` et sélectionner le `device_type`.

## Mappings DP courants (à vérifier selon firmware)
- Dimmer: `DP 1` = ON/OFF, `DP 2` = Brightness (0–100)
- Switch multi-gang: `DP 1..4` = on/off pour chaque canal
- Curtain/Garage: `DP 1` = open, `DP 2` = close, `DP 3` = stop, `DP 101` = position (0–100)

## Limitations
- Les `dps` peuvent varier selon firmware. Si un appareil ne répond pas comme prévu, récupérez le `status()` via tinytuya et ouvrez une issue.
- L'intégration nécessite le `local_key` pour le contrôle local.

## Licence
MIT — voir fichier LICENSE.

## Aide / Issues
Ouvrez une issue sur le dépôt GitHub : `https://github.com/SoFarSoGood86/moes_mini_module/issues`
