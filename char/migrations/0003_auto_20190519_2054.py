# Generated by Django 2.2.1 on 2019-05-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('char', '0002_auto_20190519_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='char',
            name='class_field',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Novice'), (1, 'Swordman'), (2, 'Magician'), (3, 'Archer'), (4, 'Acolyte'), (5, 'Merchant'), (6, 'Thief'), (7, 'Knight'), (8, 'Priest'), (9, 'Wizard'), (10, 'Blacksmith'), (11, 'Hunter'), (12, 'Assassin'), (13, 'Knight (Peco)'), (14, 'Crusader'), (15, 'Monk'), (16, 'Sage'), (17, 'Rogue'), (18, 'Alchemist'), (19, 'Bard'), (20, 'Dancer'), (21, 'Crusader (Peco)'), (22, 'Wedding (Deprecated)'), (23, 'Super Novice'), (24, 'Gunslinger'), (25, 'Ninja'), (4001, 'Novice High'), (4002, 'Swordman High'), (4003, 'Magician High'), (4004, 'Archer High'), (4005, 'Acolyte High'), (4006, 'Merchant High'), (4007, 'Thief High'), (4008, 'Lord Knight'), (4009, 'High Priest'), (4010, 'High Wizard'), (4011, 'Whitesmith'), (4012, 'Sniper'), (4013, 'Assassin Cross'), (4014, 'Lord Knight (Peco)'), (4015, 'Paladin'), (4016, 'Champion'), (4017, 'Professor'), (4018, 'Stalker'), (4019, 'Creator'), (4020, 'Clown'), (4021, 'Gypsy'), (4022, 'Paladin (Peco)'), (4023, 'Baby Novice'), (4024, 'Baby Swordman'), (4025, 'Baby Magician'), (4026, 'Baby Archer'), (4027, 'Baby Acolyte'), (4028, 'Baby Merchant'), (4029, 'Baby Thief'), (4030, 'Baby Knight'), (4031, 'Baby Priest'), (4032, 'Baby Wizard'), (4033, 'Baby Blacksmith'), (4034, 'Baby Hunter'), (4035, 'Baby Assassin'), (4036, 'Baby Knight (Peco)'), (4037, 'Baby Crusader'), (4038, 'Baby Monk'), (4039, 'Baby Sage'), (4040, 'Baby Rogue'), (4041, 'Baby Alchemist'), (4042, 'Baby Bard'), (4043, 'Baby Dancer'), (4044, 'Baby Crusader (Peco)'), (4045, 'Baby Super Novice'), (4046, 'Taekwon'), (4047, 'Star Gladiator'), (4048, 'Star Gladiator (Union)'), (4049, 'Soul Linker'), (4050, 'Gangsi (Bongun/Munak)'), (4051, 'Death Knight'), (4052, 'Dark Collector'), (4054, 'Rune Knight (Regular)'), (4055, 'Warlock (Regular)'), (4056, 'Ranger (Regular)'), (4057, 'Arch Bishop (Regular)'), (4058, 'Mechanic (Regular)'), (4059, 'Guillotine Cross (Regular)'), (4060, 'Rune Knight (Trans)'), (4061, 'Warlock (Trans)'), (4062, 'Ranger (Trans)'), (4063, 'Arch Bishop (Trans)'), (4064, 'Mechanic (Trans)'), (4065, 'Guillotine Cross (Trans)'), (4066, 'Royal Guard (Regular)'), (4067, 'Sorcerer (Regular)'), (4068, 'Minstrel (Regular)'), (4069, 'Wanderer (Regular)'), (4070, 'Sura (Regular)'), (4071, 'Genetic (Regular)'), (4072, 'Shadow Chaser (Regular)'), (4073, 'Royal Guard (Trnas)'), (4074, 'Sorcerer (Trans)'), (4075, 'Minstrel (Trans)'), (4076, 'Wanderer (Trans)'), (4077, 'Sura (Trans)'), (4078, 'Genetic (Trans)'), (4079, 'Shadow Chaser (Trans)'), (4080, 'Rune Knight (Dragon) (Regular)'), (4081, 'Rune Knight (Dragon) (Trans)'), (4082, 'Royal Guard (Gryphon) (Regular)'), (4083, 'Royal Guard (Gryphon) (Trans)'), (4084, 'Ranger (Warg) (Regular)'), (4085, 'Ranger (Warg) (Trans)'), (4086, 'Mechanic (Mado) (Regular)'), (4087, 'Mechanic (Mado) (Trans)'), (4096, 'Baby Rune Knight'), (4097, 'Baby Warlock'), (4098, 'Baby Ranger'), (4099, 'Baby Arch Bishop'), (4100, 'Baby Mechanic'), (4101, 'Baby Guillotine Cross'), (4102, 'Baby Royal Guard'), (4103, 'Baby Sorcerer'), (4104, 'Baby Minstrel'), (4105, 'Baby Wanderer'), (4106, 'Baby Sura'), (4107, 'Baby Genetic'), (4108, 'Baby Shadow Chaser'), (4109, 'Baby Rune Knight (Dragon)'), (4110, 'Baby Royal Guard (Gryphon)'), (4111, 'Baby Ranger (Warg)'), (4112, 'Baby Mechanic (Mado)'), (4190, 'Super Novice (Expanded)'), (4191, 'Super Baby (Expanded)'), (4211, 'Kagerou'), (4212, 'Oboro'), (4215, 'Rebellion'), (4218, 'Summoner'), (4220, 'Baby Summoner'), (4222, 'Baby Ninja'), (4223, 'Baby Kagerou'), (4224, 'Baby Oboro'), (4225, 'Baby Taekwon'), (4226, 'Baby Star Gladiator'), (4227, 'Baby Soul Linker'), (4228, 'Baby Gunslinger'), (4229, 'Baby Rebellion'), (4238, 'Baby Star Gladiator (Union)'), (4239, 'Star Emperor'), (4240, 'Soul Reaper'), (4241, 'Baby Star Emperor'), (4242, 'Baby Soul Reaper'), (4243, 'Star Emperor (Union)'), (4244, 'Baby Star Emperor (Union)')], db_column='class', help_text='Do not change manually, use in-game commands instead.'),
        ),
    ]