#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.vertical_speed = 0 if self.name != 'Enemy3' else choice((1, -1))

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.name == 'Enemy3':
            if self.rect.bottom >= WIN_HEIGHT or self.rect.top <= 0:
                self.vertical_speed = -self.vertical_speed  # Inverta a direção

        self.rect.centery += self.vertical_speed

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
