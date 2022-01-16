#!/usr/bin/env bash
set -eux

cp -f {luftctl,panel}.kicad_pro
kikit panelize -p panelize.json {luftctl,panel}.kicad_pcb
rm panel.kicad_pro
