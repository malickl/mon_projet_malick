import simpleaudio as sa

def afficher_menu(options):
    from tty_menu import tty_menu
    pos = tty_menu(options)
    return pos



def changer_musique(nouvelle_musique):
    sa.stop_all()
    nouvelle_musique_objet = sa.WaveObject.from_wave_file(nouvelle_musique)
    nouvelle_musique_objet.play()



def jouer_effet_sonore(nom_fichier):
    effet_sonore = sa.WaveObject.from_wave_file(nom_fichier)
    effet_sonore.play()





