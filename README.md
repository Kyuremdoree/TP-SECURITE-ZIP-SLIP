# TP-SECURITE-ZIP-SLIP

# Sujet

vous êtes aujourd'hui à la foi, l'attaquant et la victime.

### Etape Attaquant

Vous êtes un professeur et vous voulez tester l'honnêteté de vos élèves.<br> Pour cela, vous avez eu une petite idée : après avoir appris qu'il est possible d'exécuter du code lorsqu'une personne dézippe un dossier, vous allez implémenter un programme malveillant dans un fichier ZIP afin qu'il s'exécute lors d'un dézippage non sécurisé. Cela s'appelle une attaque <strong>Zip Slip</strong>.

Pour mettre votre plan à exécution, vous allez d'abord récupérer le programme Python suivant :

`Create_EvilZip.py` 

Vous aurez besoin de Python pour exécuter le programme, et voici comment l'utiliser :
```
python Create_EvilZip.py dossier.zip
```

Cependant, vous devrez réaliser certaines modifications dans le programme de création du ZIP piégé.

Maintenant, vous avez un ZIP totalement infecté. Celui-ci exécutera donc le programme que vous avez intégré dans votre archive ZIP malveillante.

Vous enverrez à votre victime le fichier ZIP et le programme `UnZip_Program.py`, qui est vulnérable à ce type d'attaque car il manque une vérification.

### Etape Victime

notre victime va donc recevoir un fichier zip contenant tous ces "précieuses corrections"

`python UnZip_program.py dossier.zip` : maintenant executer ce programme sur votre dossier zipper<br>

Comme vous vous en doutiez, le piège s'est activé !
Mais il existe un moyen de sécuriser le dézippage. Pour cela, vous avez à votre disposition :
`UnZip_Secured_program.py`

Vous devez donc remplacer les `TODO()`