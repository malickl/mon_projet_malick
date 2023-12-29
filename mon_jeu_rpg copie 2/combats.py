import time
from colorama import Fore, Style
import fonction_utile as fonction
import random
import sys 

def afficher_texte_progressif(texte, couleur=Fore.WHITE, vitesse=0.001):
    print(couleur, end='', flush=True)
    for lettre in texte:
        print(lettre, end='', flush=True)
        time.sleep(vitesse)
    print(Style.RESET_ALL)  # Réinitialise la couleur du texte à sa valeur par défaut



class Item:
    def __init__(self, nom, durabilite):
        self.nom = nom
        self.durabilite = durabilite

    def utiliser(self, joueur, ennemi):
        pass  


# different item
          
class Epee_sacre(Item):
    def __init__(self):
        super().__init__('epee sacré', 10)
        self.degats = 100  

    def __str__(self):
        return f"degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous attaquez avec l'épée sacré ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif('votre épee sacré est brisé')

class epee_geante(Item):
    def __init__(self):
        super().__init__('épée géante', 20)
        self.degats = 60  

    def __str__(self):
        return f"degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous attaquez avec épée géante ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif('votre épée géante est brisé')

class PotionSoin(Item):
    def __init__(self):
        super().__init__('potion de soin',1)
        self.soins = 20  
        self.quantite = 1

    def utiliser(self, joueur, ennemi):
        if joueur.nombre_potions > 0:
            joueur.pv += self.soins
            joueur.nombre_potions -= 1  
            afficher_texte_progressif(f"Vous avez utilisé une potion de soin ! Vous récupérez {self.soins} PV.\n", couleur=Fore.GREEN)
        else:
            afficher_texte_progressif("Vous n'avez plus de potions de soin.\n", couleur=Fore.RED)

class Orbre_eau(Item):
    def __init__(self):
        super().__init__("orbre d'eau",1)
        self.soins = 250  

    def __str__(self):
        return f"soin: {self.soins},durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
            joueur.pv += self.soins
            afficher_texte_progressif(f"Vous avez utilisé l'orbre d'eau ! Vous récupérez {self.soins} PV.\n", couleur=Fore.GREEN)
            self.durabilite -= 1
            if self.durabilite == 0:
                afficher_texte_progressif("Vous n'avez plus d'orbre d'eau'.\n", couleur=Fore.RED)

class Epee_diamant(Item):
    def __init__(self):
        super().__init__('epee en diamant', 10)
        self.degats = 30 

    def __str__(self):
        return f"degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous attaquez avec l'épée en diamant ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif('votre épee en diamant est brisé')

class baton_magique(Item):
    def __init__(self):
        super().__init__('baton magique', 3)
        self.degats = 300 

    def __str__(self):
        return f"degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous attaquez avec le baton ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif('votre baton est brisé')

class amulette_imperial(Item):
    def __init__(self):
        super().__init__("amulette_imperial",1)
        self.soins = 3000  

    def __str__(self):
        return f"capacité de soin: {self.soins}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
            joueur.pv += self.soins 
            afficher_texte_progressif(f"Vous avez utilisé l'amulette_imperial ! Vous récupérez {self.soins} PV.\n", couleur=Fore.GREEN)
            self.durabilite -= 1
            if self.durabilite == 0:
                afficher_texte_progressif("Vous n'avez plus d'amulette_imperial'.\n", couleur=Fore.RED)

class armure_en_diamant(Item):
    def __init__(self):
        super().__init__('armure en diamant', 3)
        self.degats = 300 

    def __str__(self):
        return f"degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous attaquez avec le baton ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif('votre baton est brisé')

class lance_missile(Item):
    def __init__(self):
        super().__init__('lance missile', 1)
        self.degats = 500 

    def __str__(self):
        return f"degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous attaquez avec le lance missile ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif('votre lance missile est brisé')

class bâton_mystérieux(Item):
    def __init__(self):
        super().__init__('bâton mystérieux', 1)
        self.degats = 3000 

    def __str__(self):
        return f"degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous attaquez avec le bâton mystérieux ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif('votre bâton mystérieux est brisé')

class boule_feu(Item):
    def __init__(self):
        super().__init__('boule de feu', 20)
        self.degats = 30 

    def __str__(self):
        return f"boule de feu, degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous lanez une boule de feu ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif("vous n'avez plus d'energie magique de feu")

class boule_glace(Item):
    def __init__(self):
        super().__init__('boule de glace', 30)
        self.degats = 20 

    def __str__(self):
        return f"boule de glace, degats: {self.degats}, durabilité: {self.durabilite}"

    def utiliser(self, joueur, ennemi):
        ennemi.pv -= self.degats
        self.durabilite -= 1
        afficher_texte_progressif(f"Vous lanez une boule de glace ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)
        if self.durabilite == 0:
            afficher_texte_progressif("vous n'avez plus d'energie magique de glace")




# different mob
class Joueur:

    def __init__(self, pv, att, xp):
        self.pv = pv
        self.att = att
        self.xp = xp
        self.sac_a_dos = []
        self.nombre_potions = 0
        self.a_visite_etage = False
        self.a_visite_sous_sol = False


    def __str__(self):
        return f"PV: {self.pv}, Attaque: {self.att}, XP: {self.xp}"
    

    def attaquer(self, ennemi):
        ennemi.pv -= self.att
        afficher_texte_progressif(f"Vous attaquez ! L'ennemi a maintenant {ennemi.pv} PV.\n", couleur=Fore.BLUE)

    def exp(self, ennemi):
        self.xp += ennemi.xp
        afficher_texte_progressif(f"Vous avez gagné {ennemi.xp} xp.\n", couleur=Fore.BLUE)

        if self.xp >= 100:  # Vérifie si le joueur a atteint un multiple de 100 XP
            bonus = self.xp // 100  # Calcule le nombre de paliers de 100 XP atteints
            self.pv += bonus * 5  # Augmente les points de vie
            self.att += bonus * 5  # Augmente l'attaque
            afficher_texte_progressif(f"Vous avez gagné des bonus de caractéristiques ! PV +{bonus*5}, Attaque +{bonus*5}\n", couleur=Fore.GREEN)
            self.xp %= 100  # Réinitialise l'XP restant après l'augmentation des caractéristiques

    def ajouter_item_sac_a_dos(self, item):
        for i in self.sac_a_dos:
            if isinstance(i, PotionSoin) and isinstance(item, PotionSoin):
                i.quantite += 1
                return
        self.sac_a_dos.append(item)
   
    def tour(self, ennemi):
        afficher_texte_progressif("Tour du joueur :\n", couleur=Fore.BLUE)

        choix_utilisateur=fonction.afficher_menu(['Attaquer','Utiliser un item'])

        if choix_utilisateur == 0:
            self.attaquer(ennemi)
        elif choix_utilisateur == 1:
            self.utiliser_item(ennemi) 
        return False

    def utiliser_item(self, ennemi):
        if not self.sac_a_dos:
            afficher_texte_progressif("Votre sac à dos est vide.\n", couleur=Fore.BLUE)
            return

        afficher_texte_progressif("Voici les items dans votre sac à dos :\n", couleur=Fore.BLUE)
        choix_item = fonction.afficher_menu([item.nom for item in self.sac_a_dos])

        if choix_item < len(self.sac_a_dos):
            item_utilise = self.sac_a_dos[choix_item]
            if isinstance(item_utilise, PotionSoin):
                item_utilise.quantite -= 1
                afficher_texte_progressif(f"Vous avez utilisé une potion de soin ! Vous récupérez {item_utilise.soins} PV.\n", couleur=Fore.GREEN)
                if item_utilise.quantite <= 0:
                    self.sac_a_dos.pop(choix_item)
                    afficher_texte_progressif("Vous n'avez plus de potions de soin.\n", couleur=Fore.RED)                  
            else:
                item_utilise.utiliser(self, ennemi)
                if item_utilise.durabilite <= 0:
                    afficher_texte_progressif(f"Votre {item_utilise.nom} est maintenant brisé et ne peut plus être utilisé.\n", couleur=Fore.RED)
                    self.sac_a_dos.pop(choix_item)

class gobelin:
    def __init__(self, pv, att, xp):
        self.pv = pv
        self.att = att
        self.xp = xp
    def attaquer(self, joueur):
        joueur.pv -= self.att
        afficher_texte_progressif(f"Le gobelin attaque ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)

class spectre:
    def __init__(self, pv, att, xp):
        self.pv = pv
        self.att = att
        self.xp = xp
    def attaquer(self, joueur):
        joueur.pv -= self.att
        afficher_texte_progressif(f"Le spectre attaque ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)

class sirene:
    def __init__(self, pv, att, ult, xp):
        self.pv = pv
        self.att = att
        self.ult= ult
        self.xp = xp
    def attaquer(self, joueur):
        chance_utl=random.randint(1,5)
        if chance_utl==2:
            joueur.pv-=self.ult
            afficher_texte_progressif(f"La sirene fait une attaque special ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)   
        else:
            joueur.pv -= self.att
            afficher_texte_progressif(f"La sirene attaque ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)

class kraken:
    def __init__(self, pv, att, ult, xp):
        self.pv = pv
        self.att = att
        self.ult= ult
        self.xp = xp
    def attaquer(self, joueur):
        chance_utl=random.randint(1,5)
        if chance_utl==2:
            joueur.pv-=self.ult
            afficher_texte_progressif(f"Le kraken lance un jet d'ancre surpuissant ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)   
        else:
            joueur.pv -= self.att
            afficher_texte_progressif(f"Le kraken attaque avec ses tentacule! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)

class loup_géant:
    def __init__(self, pv, att, ult, xp):
        self.pv = pv
        self.att = att
        self.ult= ult
        self.xp = xp
    def attaquer(self, joueur):
        chance_utl=random.randint(1,5)
        if chance_utl==2:
            joueur.pv-=self.ult
            afficher_texte_progressif(f"Le loup géant lance une attaque ultra tranchante avec sonn épée ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)   
        else:
            joueur.pv -= self.att
            afficher_texte_progressif(f"Le loup géant attaque avec ses griffes! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)

class arraignée:
    def __init__(self, pv, att, ult, xp):
        self.pv = pv
        self.att = att
        self.ult= ult
        self.xp = xp
    def attaquer(self, joueur):
        chance_utl=random.randint(1,3)
        if chance_utl==2:
            joueur.pv-=self.ult
            afficher_texte_progressif(f"L'arraignée attaque avec une toile acidifié ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)   
        else:
            joueur.pv -= self.att
            afficher_texte_progressif(f"L'arraignée attaque avec ses pattes! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)

# 3 commandants

class chevalier_noir:
    def __init__(self, pv, att, ult, xp):
        self.pv = pv
        self.att = att
        self.ult= ult
        self.xp = xp

    def __str__(self):
        return f"PV: {self.pv}, Attaque: {self.att}, ultime: {self.ult}"
    
    def attaquer(self, joueur):
        chance_utl=random.randint(1,5)
        if chance_utl==2:
            joueur.pv-=self.ult
            afficher_texte_progressif(f"Le chevalier noir lance une super attaque tranchante ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)   
        else:
            joueur.pv -= self.att
            afficher_texte_progressif(f"Le chevalier noir attaque! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)

class vampire_ancien:
    def __init__(self, pv, att, ult, xp):
        self.pv = pv
        self.att = att
        self.ult= ult
        self.xp = xp

    def __str__(self):
        return f"PV: {self.pv}, Attaque: {self.att}, ultime: {self.ult}"

    def attaquer(self, joueur, vampire_ancien):
        chance_utl=random.randint(1,3)
        if chance_utl==2:
            joueur.pv-=self.ult
            afficher_texte_progressif(f"Le vampire ancien vous mord ! Vous avez maintenant {joueur.pv} PV et lui recupère 40 pv.\n", couleur=Fore.RED)
            vampire_ancien.pv +=50   
        else:
            joueur.pv -= self.att
            afficher_texte_progressif(f"Le vampire ancien attaque ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)

class dragon_millénaire :
    def __init__(self, pv, att, ult, xp):
        self.pv = pv
        self.att = att
        self.ult= ult
        self.xp = xp

    def __str__(self):
        return f"PV: {self.pv}, Attaque: {self.att}, ultime: {self.ult}"

    def attaquer(self, joueur):
        chance_utl=random.randint(1,5)
        if chance_utl==2:
            joueur.pv-=self.ult
            afficher_texte_progressif(f"Le dragon millénaire lance une boule de larve de 1000 degré ! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)   
        else:
            joueur.pv -= self.att
            afficher_texte_progressif(f"Le dragon millénaire attaque avec sa queue ultra longue! Vous avez maintenant {joueur.pv} PV.\n", couleur=Fore.RED)





















def combat(joueur, ennemi):
    afficher_texte_progressif("le combat commence\n", couleur=Fore.GREEN)
    joueur_a_fui = False

    while joueur.pv > 0 and ennemi.pv > 0 and not joueur_a_fui:
        joueur_a_fui = joueur.tour(ennemi)

        if ennemi.pv <= 0:
            afficher_texte_progressif("Vous avez vaincu l'ennemi' !", couleur=Fore.BLUE)
            joueur.exp(ennemi)
            break

        if not joueur_a_fui:
            ennemi.attaquer(joueur)
            if joueur.pv <= 0:
                
                afficher_texte_progressif("L'ennemi vous a vaincu !", couleur=Fore.BLUE)
                exit()





""" joueur1 = Joueur(pv=300, att=20, xp=0)

# joueur1.ajouter_item_sac_a_dos(PotionSoin())
# joueur1.ajouter_item_sac_a_dos(PotionSoin())
# snake_lvl_10 = snake(pv=1000, att=80, xp=101)
# combat(joueur1, snake_lvl_10)


# print(joueur1)


sirene= sirene(pv=300, att=30,ult=55, xp=150)
combat(joueur1, sirene)  """











