import pygame

an_left1 = [
           pygame.image.load('pers/first_level/left1.png'), pygame.image.load('pers/first_level/left2.png'),
           pygame.image.load('pers/first_level/left3.png'), pygame.image.load('pers/first_level/left4.png'),
           pygame.image.load('pers/first_level/left5.png'), pygame.image.load('pers/first_level/left6.png')
        ]
an_right1 = [
            pygame.image.load('pers/first_level/right1.png'), pygame.image.load('pers/first_level/right2.png'),
            pygame.image.load('pers/first_level/right3.png'), pygame.image.load('pers/first_level/right4.png'),
            pygame.image.load('pers/first_level/right5.png'), pygame.image.load('pers/first_level/right6.png')
        ]
an_state1 = pygame.image.load('pers/first_level/state.png')

an_left3 = [
            pygame.image.load('pers/third_level/left1.png'), pygame.image.load('pers/third_level/left2.png'),
            pygame.image.load('pers/third_level/left3.png'), pygame.image.load('pers/third_level/left4.png'),
            pygame.image.load('pers/third_level/left5.png'), pygame.image.load('pers/third_level/left6.png')
        ]

an_right3 = [
            pygame.image.load('pers/third_level/right1.png'), pygame.image.load('pers/third_level/right2.png'),
            pygame.image.load('pers/third_level/right3.png'), pygame.image.load('pers/third_level/right4.png'),
            pygame.image.load('pers/third_level/right5.png'), pygame.image.load('pers/third_level/right6.png')
        ]

an_state3 = pygame.image.load('pers/third_level/state.png')


an_menu = [
           pygame.image.load('background/menu/menu1.png'), pygame.image.load('background/menu/menu2.png'),
           pygame.image.load('background/menu/menu3.png'), pygame.image.load('background/menu/menu4.png'),
           pygame.image.load('background/menu/menu5.png'), pygame.image.load('background/menu/menu6.png'),
           pygame.image.load('background/menu/menu7.png'), pygame.image.load('background/menu/menu8.png'),
           pygame.image.load('background/menu/menu9.png'), pygame.image.load('background/menu/menu10.png'),
           pygame.image.load('background/menu/menu11.png'), pygame.image.load('background/menu/menu12.png'),
           pygame.image.load('background/menu/menu13.png'), pygame.image.load('background/menu/menu14.png'),
           pygame.image.load('background/menu/menu15.png'), pygame.image.load('background/menu/menu16.png'),
           pygame.image.load('background/menu/menu17.png'), pygame.image.load('background/menu/menu18.png'),
           pygame.image.load('background/menu/menu19.png'), pygame.image.load('background/menu/menu20.png'),
           pygame.image.load('background/menu/menu21.png'), pygame.image.load('background/menu/menu22.png'),
           pygame.image.load('background/menu/menu23.png'), pygame.image.load('background/menu/menu24.png'),
           pygame.image.load('background/menu/menu25.png'), pygame.image.load('background/menu/menu26.png'),
           pygame.image.load('background/menu/menu27.png'), pygame.image.load('background/menu/menu28.png'),
           pygame.image.load('background/menu/menu29.png'), pygame.image.load('background/menu/menu30.png'),
           pygame.image.load('background/menu/menu31.png'), pygame.image.load('background/menu/menu32.png'),
           pygame.image.load('background/menu/menu33.png'), pygame.image.load('background/menu/menu34.png'),
           pygame.image.load('background/menu/menu35.png'), pygame.image.load('background/menu/menu36.png'),
           pygame.image.load('background/menu/menu37.png'), pygame.image.load('background/menu/menu38.png'),
           pygame.image.load('background/menu/menu39.png'), pygame.image.load('background/menu/menu40.png'),
           pygame.image.load('background/menu/menu41.png'), pygame.image.load('background/menu/menu42.png'),
           pygame.image.load('background/menu/menu43.png'), pygame.image.load('background/menu/menu44.png'),
           pygame.image.load('background/menu/menu45.png'), pygame.image.load('background/menu/menu46.png'),
           pygame.image.load('background/menu/menu47.png'), pygame.image.load('background/menu/menu48.png'),
           pygame.image.load('background/menu/menu49.png'), pygame.image.load('background/menu/menu50.png'),
           pygame.image.load('background/menu/menu51.png'), pygame.image.load('background/menu/menu52.png'),
           pygame.image.load('background/menu/menu53.png'), pygame.image.load('background/menu/menu54.png'),
           pygame.image.load('background/menu/menu55.png'), pygame.image.load('background/menu/menu56.png'),
           pygame.image.load('background/menu/menu57.png'), pygame.image.load('background/menu/menu58.png'),
           pygame.image.load('background/menu/menu59.png'), pygame.image.load('background/menu/menu60.png')
        ]

an_axe = [
           [
               pygame.image.load('danger/axe1.png'), pygame.image.load('danger/axe2.png'),
               pygame.image.load('danger/axe3.png'), pygame.image.load('danger/axe4.png'),
               pygame.image.load('danger/axe5.png'), pygame.image.load('danger/axe6.png')
           ],
           [
               pygame.image.load('danger/axe2.png'), pygame.image.load('danger/axe3.png'),
               pygame.image.load('danger/axe4.png'), pygame.image.load('danger/axe5.png'),
               pygame.image.load('danger/axe6.png'), pygame.image.load('danger/axe1.png')
           ],
           [
               pygame.image.load('danger/axe3.png'), pygame.image.load('danger/axe4.png'),
               pygame.image.load('danger/axe5.png'), pygame.image.load('danger/axe6.png'),
               pygame.image.load('danger/axe1.png'), pygame.image.load('danger/axe2.png')
           ],
           [
               pygame.image.load('danger/axe4.png'), pygame.image.load('danger/axe5.png'),
               pygame.image.load('danger/axe6.png'), pygame.image.load('danger/axe1.png'),
               pygame.image.load('danger/axe2.png'), pygame.image.load('danger/axe3.png')
           ],
           [
               pygame.image.load('danger/axe5.png'), pygame.image.load('danger/axe6.png'),
               pygame.image.load('danger/axe1.png'), pygame.image.load('danger/axe2.png'),
               pygame.image.load('danger/axe3.png'), pygame.image.load('danger/axe4.png')
           ],
           [
               pygame.image.load('danger/axe6.png'), pygame.image.load('danger/axe1.png'),
               pygame.image.load('danger/axe2.png'), pygame.image.load('danger/axe3.png'),
               pygame.image.load('danger/axe4.png'), pygame.image.load('danger/axe5.png')
           ]
        ]

an_wood = [
            [
                pygame.image.load('increase_score/wood1.png'), pygame.image.load('increase_score/wood2.png'),
                pygame.image.load('increase_score/wood3.png'), pygame.image.load('increase_score/wood4.png')
            ],
            [
                pygame.image.load('increase_score/wood2.png'), pygame.image.load('increase_score/wood3.png'),
                pygame.image.load('increase_score/wood4.png'), pygame.image.load('increase_score/wood1.png')
            ],
            [
                pygame.image.load('increase_score/wood3.png'), pygame.image.load('increase_score/wood4.png'),
                pygame.image.load('increase_score/wood1.png'), pygame.image.load('increase_score/wood2.png')
            ],
            [
                pygame.image.load('increase_score/wood4.png'), pygame.image.load('increase_score/wood1.png'),
                pygame.image.load('increase_score/wood2.png'), pygame.image.load('increase_score/wood3.png')
            ]
        ]

an_bg_1 = [
         pygame.image.load('background/bg_first_lvl/bg1.png'), pygame.image.load('background/bg_first_lvl/bg2.png'),
         pygame.image.load('background/bg_first_lvl/bg3.png'), pygame.image.load('background/bg_first_lvl/bg4.png'),
         pygame.image.load('background/bg_first_lvl/bg5.png'), pygame.image.load('background/bg_first_lvl/bg6.png'),
         pygame.image.load('background/bg_first_lvl/bg7.png'), pygame.image.load('background/bg_first_lvl/bg8.png'),
         pygame.image.load('background/bg_first_lvl/bg9.png'), pygame.image.load('background/bg_first_lvl/bg10.png'),
         pygame.image.load('background/bg_first_lvl/bg11.png'), pygame.image.load('background/bg_first_lvl/bg12.png'),
         pygame.image.load('background/bg_first_lvl/bg13.png'), pygame.image.load('background/bg_first_lvl/bg14.png'),
         pygame.image.load('background/bg_first_lvl/bg15.png'), pygame.image.load('background/bg_first_lvl/bg16.png')
     ]
an_bg_2 = [
        pygame.image.load('background/bg_second_lvl/bg1.png'), pygame.image.load('background/bg_second_lvl/bg2.png'),
        pygame.image.load('background/bg_second_lvl/bg3.png'), pygame.image.load('background/bg_second_lvl/bg4.png'),
        pygame.image.load('background/bg_second_lvl/bg5.png'), pygame.image.load('background/bg_second_lvl/bg6.png'),
        pygame.image.load('background/bg_second_lvl/bg7.png'), pygame.image.load('background/bg_second_lvl/bg8.png'),
        pygame.image.load('background/bg_second_lvl/bg9.png'), pygame.image.load('background/bg_second_lvl/bg10.png'),
        pygame.image.load('background/bg_second_lvl/bg11.png'), pygame.image.load('background/bg_second_lvl/bg12.png'),
        pygame.image.load('background/bg_second_lvl/bg13.png'), pygame.image.load('background/bg_second_lvl/bg14.png'),
        pygame.image.load('background/bg_second_lvl/bg15.png'), pygame.image.load('background/bg_second_lvl/bg16.png')
    ]
an_bg_3 = [
        pygame.image.load('background/bg_third_lvl/bg1.png'), pygame.image.load('background/bg_third_lvl/bg2.png'),
        pygame.image.load('background/bg_third_lvl/bg3.png'), pygame.image.load('background/bg_third_lvl/bg4.png'),
        pygame.image.load('background/bg_third_lvl/bg5.png'), pygame.image.load('background/bg_third_lvl/bg6.png'),
        pygame.image.load('background/bg_third_lvl/bg7.png'), pygame.image.load('background/bg_third_lvl/bg8.png'),
        pygame.image.load('background/bg_third_lvl/bg9.png'), pygame.image.load('background/bg_third_lvl/bg10.png'),
        pygame.image.load('background/bg_third_lvl/bg11.png'), pygame.image.load('background/bg_third_lvl/bg12.png'),
        pygame.image.load('background/bg_third_lvl/bg13.png'), pygame.image.load('background/bg_third_lvl/bg14.png'),
        pygame.image.load('background/bg_third_lvl/bg15.png'), pygame.image.load('background/bg_third_lvl/bg16.png')
    ]
an_bg_4 = [
        pygame.image.load('background/bg_fourth_lvl/bg1.png'), pygame.image.load('background/bg_fourth_lvl/bg2.png'),
        pygame.image.load('background/bg_fourth_lvl/bg3.png'), pygame.image.load('background/bg_fourth_lvl/bg4.png'),
        pygame.image.load('background/bg_fourth_lvl/bg5.png'), pygame.image.load('background/bg_fourth_lvl/bg6.png'),
        pygame.image.load('background/bg_fourth_lvl/bg7.png'), pygame.image.load('background/bg_fourth_lvl/bg8.png'),
        pygame.image.load('background/bg_fourth_lvl/bg9.png'), pygame.image.load('background/bg_fourth_lvl/bg10.png'),
        pygame.image.load('background/bg_fourth_lvl/bg11.png'), pygame.image.load('background/bg_fourth_lvl/bg12.png'),
        pygame.image.load('background/bg_fourth_lvl/bg13.png'), pygame.image.load('background/bg_fourth_lvl/bg14.png'),
        pygame.image.load('background/bg_fourth_lvl/bg15.png'), pygame.image.load('background/bg_fourth_lvl/bg16.png')
    ]
an_bg_5 = [
        pygame.image.load('background/bg_fifth_lvl/bg1.png'), pygame.image.load('background/bg_fifth_lvl/bg2.png'),
        pygame.image.load('background/bg_fifth_lvl/bg3.png'), pygame.image.load('background/bg_fifth_lvl/bg4.png'),
        pygame.image.load('background/bg_fifth_lvl/bg5.png'), pygame.image.load('background/bg_fifth_lvl/bg6.png'),
        pygame.image.load('background/bg_fifth_lvl/bg7.png'), pygame.image.load('background/bg_fifth_lvl/bg8.png'),
        pygame.image.load('background/bg_fifth_lvl/bg9.png'), pygame.image.load('background/bg_fifth_lvl/bg10.png'),
        pygame.image.load('background/bg_fifth_lvl/bg11.png'), pygame.image.load('background/bg_fifth_lvl/bg12.png'),
        pygame.image.load('background/bg_fifth_lvl/bg13.png'), pygame.image.load('background/bg_fifth_lvl/bg14.png'),
        pygame.image.load('background/bg_fifth_lvl/bg15.png'), pygame.image.load('background/bg_fifth_lvl/bg16.png')
    ]

an_drop = [
           pygame.image.load('upgrades/water1.png'), pygame.image.load('upgrades/water2.png'),
           pygame.image.load('upgrades/water3.png'), pygame.image.load('upgrades/water4.png')
      ]

an_bag = [
          pygame.image.load('increase_score/GU1.png'), pygame.image.load('increase_score/GU2.png')
      ]

an_flower = [
             pygame.image.load('increase_score/f1.png'), pygame.image.load('increase_score/f2.png'),
             pygame.image.load('increase_score/f3.png')
         ]
