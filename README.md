<img width="1463" height="366" alt="MOES_HA_HACS" src="https://github.com/user-attachments/assets/d049a712-5e15-422d-8f18-a6926ce2339f" />


# MOES Mini Module Intelligent (local)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz)
[![License](https://img.shields.io/github/license/SoFarSoGood86/moes_mini_module)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/SoFarSoGood86/costway_climate)](https://github.com/SoFarSoGood86/moes_mini_module/releases)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Integration-41BDF5)](https://www.home-assistant.io/)

## Description
Cette intégration Home Assistant permet le contrôle en local (TuyaLan Protocol) sans passer par le cloud, des modules MOES Mini Intelligent (dimmer, switch, curtain, garage) via la bibliothèque [`tinytuya`](https://github.com/jasonacox/tinytuya).
Elle regroupe plusieurs types d'appareils dans une intégration unique pour une maintenance simplifiée.

## Modules supportés
- MOES Mini Dimmer module 1 gang (dimmer_1)
- MOES Mini Dimmer module 2 gang (dimmer_2)
- MOES Mini Switch module 1 gang (switch_1)
- MOES Mini Switch module 2 gang (switch_2)
- MOES Mini Switch module 3 gang (switch_3)
- MOES Mini Switch module 4 gang (switch_4)
- MOES Mini Smart Curtain Switch module (curtain)
- MOES Mini Smart Garage Door module (garage)

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
