'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import pygame,sys

pygame.init();#initialize pygame
screen=pygame.display.set_mode((640,460))#create the screen
pygame.display.set_caption("Pygame tutorial")#sets the screen name
pygame.time.delay(2000)#paauses for 2 seconds
pygame.quit()
