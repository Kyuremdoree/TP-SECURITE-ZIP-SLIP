# TP-SECURITE-ZIP-SLIP

# Sujet

vous êtes aujourd'hui à la foi, l'attaquant et la victime.

### Etape Attaquant

Vous êtes un professeur et vous voulez tester la franchise de vos élèves.<br>
Pour faire cela vous avez eu une petit idée, après avoir appris qu'il était possible d'executer du code lorsque qu'une personne dezip un dossier, on va donc implémenté un programme malveillant dans notre zip afin qu'il s'éxecuter lors d'un dézippage non sécurisé on appel ça le <strong>Zip Slip</strong>.
afin de mettre votre plan à execution vous allez d'abord récupérer le programme python :

```
Create_EvilZip.py
```

vous aurez besoin de python pour executer le programme et voici comment l'utilisé :
```
python Create_EvilZip.py dossier.zip
```

Cependant vous devrez vous même réaliser certaine tâche dans le programme de création du zip piègé.

maintenant vous avez un zip totalement infecté, celui-ci executera donc le programme que vous avez intégrer dans votre zippeur malveillant.

Vous enverrez à votre victime, le zip et le UnZip_Program.py qui est vunérable à ce type d'attaque car il manque une vérification.
### Etape Victime

notre victime va donc recevoir un fichier zip contenant tous ces "précieuse correction"

`python UnZip_program.py dossier.zip` : maintenant executer ce programme sur votre dossier zipper<br>

Comme vous pouviez vous en doutez le piège c'est donc activé !

Mais il y a un moyen de sécurisé le dézipage, pour cela vous avez :
```
UnZip_Secured.py
```