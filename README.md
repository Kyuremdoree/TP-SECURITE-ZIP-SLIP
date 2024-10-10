# TP-SECURITE-ZIP-SLIP

# Sujet

vous êtes aujourd'hui à la foi, l'attaquant et la victime.

### Etape Attaquant

Vous êtes un professeur et vous voulez tester l'honnêteté de vos élèves.<br> Pour cela, vous avez eu une petite idée : après avoir appris qu'il est possible de mettre des fichier dans le pc d'une personne lorsqu'il dézippe un dossier, vous allez implémenter un programme malveillant dans un fichier ZIP afin qu'il s'exécute lors d'un dézippage non sécurisé. Cela s'appelle une attaque <strong>Zip Slip</strong>.

1) Pour mettre votre plan à exécution, vous allez d'abord récupérer le programme Python suivant :

`Create_EvilZip.py` 

Vous aurez besoin de Python / Python3 pour exécuter le programme, et voici comment l'utiliser :
```
python Create_EvilZip.py [nom_dossier].zip
```

Cependant, vous devrez réaliser certaines modifications dans le programme de création du ZIP piégé.
De plus afin que votre piège fonctionne à merveille, vous devez modifier certain droit sur quelque fichier !</br>

2) Maintenant, vous avez un ZIP totalement infecté. Celui-ci exécutera donc le programme que vous avez intégré dans votre archive ZIP malveillante.

Vous enverrez à votre victime le fichier ZIP et le programme `UnZip_Program.py`, qui est vulnérable à ce type d'attaque car il manque une vérification.

### Etape Victime

notre victime va donc recevoir un fichier zip contenant tous ces "précieuses corrections"

3) `python UnZip_program.py [nom_dossier].zip` : maintenant executer ce programme sur votre dossier zipper<br>

4) Corriger le programme juste en dessous afin de sécuriser votre programme de dézippage
`UnZip_Secured_program.py`

Vous devez donc remplacer les `TODO()` en prennant en compte les indications donné dans le programme.</br>

5) Quel autres moyenne selon vous, la victime aurait pu mettre en place pour se protéger de la faille Zip Slip
