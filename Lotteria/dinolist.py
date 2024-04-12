class CommandBuilder:
    def __init__(self, blueprint_path, name="", stats="", color="", arg1="", arg2=0, arg3=1, arg4=0, 
                 arg5="0,0,0,0,0,0,0,0", arg6="0,0,0,0,0,0,0,0", arg7="Generated", arg8=0, arg9=0, arg10="", 
                 arg11="", arg12="", arg13=0, arg14=0, arg15="", arg16=0, arg17=0, arg18=0, arg19=20, arg20=20):
        self.blueprint_path = blueprint_path
        self.name = name
        self.stats = stats
        self.color = color
        self.args = [arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13, arg14, 
                     arg15, arg16, arg17, arg18, arg19, arg20]

    def build_command(self):
        command = 'cheat SpawnExactDino ' + f'Blueprint{self.blueprint_path}'
        if self.name:
            command += f' "{self.name}"'
        if self.stats:
            command += f' "{self.stats}"'
        if self.color:
            command += f' "{self.color}"'
        command += ' ' + ' '.join(str(arg) for arg in self.args)
        return command


# Lista predefinita dei percorsi e nomi dei dinosauri
dino_list = [
    ('/Game/Genesis2/Dinos/MilkGlider/MilkGlider_Character_BP.MilkGlider_Character_BP', "Milk Glider"),
    ('/Game/Genesis2/Dinos/Titanosaur/Titanosaur_Character_BP.Titanosaur_Character_BP', "Titanosaur"),
    ('/Game/Genesis2/Dinos/Velonasaur/Velonasaur_Character_BP.Velonasaur_Character_BP', "Velonasaur"),
    ('/Game/Genesis2/Dinos/SnowOwl/SnowOwl_Character_BP.SnowOwl_Character_BP', "Snow Owl"),
    ('/Game/Genesis2/Dinos/Managarmr/Managarmr_Character_BP.Managarmr_Character_BP', "Managarmr"),
    ('/Game/Genesis2/Dinos/Ferox/Ferox_Character_BP.Ferox_Character_BP', "Ferox"),
    ('/Game/Genesis2/Dinos/Astrodelphis/Astrodelphis_Character_BP.Astrodelphis_Character_BP', "Astrodelphis"),
    ('/Game/Genesis2/Dinos/Shadowmane/Shadowmane_Character_BP.Shadowmane_Character_BP', "Shadowmane"),
    ('/Game/Genesis2/Dinos/Magmasaur/Magmasaur_Character_BP.Magmasaur_Character_BP', "Magmasaur"),
    ('/Game/Genesis2/Dinos/Bloodstalker/Bloodstalker_Character_BP.Bloodstalker_Character_BP', "Bloodstalker"),
    ('/Game/Genesis2/Dinos/SpaceWhale/SpaceWhale_Character_BP.SpaceWhale_Character_BP', "Space Whale"),
    ('/Game/Genesis2/Dinos/Astrocetus/Astrocetus_Character_BP.Astrocetus_Character_BP', "Astrocetus"),
    ('/Game/Genesis2/Dinos/RockDrake_Character_BP.RockDrake_Character_BP', "Rock Drake"),
    ('/Game/Genesis2/Dinos/Reaper_Character_BP.Reaper_Character_BP', "Reaper"),
    ('/Game/Genesis2/Dinos/Rockwell_Character_BP.Rockwell_Character_BP', "Rockwell"),
    ('/Game/Genesis2/Dinos/Mech/Mech_Character_BP.Mech_Character_BP', "MEK"),
    # Aggiungi altri percorsi e nomi qui...
]


# Mostra all'utente i dinosauri disponibili
print("Dinosauri disponibili:")
for i, (path, name) in enumerate(dino_list, 1):
    print(f"{i}. {name} - {path}")

# Chiedi all'utente di selezionare un dinosauro
selected_index = int(input("Seleziona un dinosauro (inserisci il numero corrispondente): ")) - 1
selected_dino_path, selected_dino_name = dino_list[selected_index]

# Chiedi all'utente di inserire i dati aggiuntivi
name = input("Inserisci il nome del dinosauro (vuoto se non lo vuoi specificare): ")
stats = input("Inserisci le statistiche del dinosauro (es. 10,20,30,40,50,60,70,80): ")
color = input("Inserisci il colore del dinosauro (es. 255,255,0,0,0,0,0,0): ")

# Creare un'istanza di CommandBuilder con i valori forniti dall'utente
command_builder = CommandBuilder(selected_dino_path, name, stats, color)

# Stampare il comando generato
print("Comando generato:", command_builder.build_command())
