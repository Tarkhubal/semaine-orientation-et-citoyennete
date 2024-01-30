# Comment créer une page
## Intro
Pour créer une page, il vous faudra maîtriser un genre de langage MarkDown, qui permet de faire de belles présentations. Ne vous inquiétez pas, c'est très simple :
Le MarkDown, c'est une langage de programmation simple, utilisant une synthaxe la plus simpliste possible pour rendre un document (une page généralement) agréable à lire, tout en étant le plus fonctionnel possible. Nous avons utilisé une version de Markdown basique que nous avons modifié afin de pouvoir l'utiliser pour créer des pages Web dans un style pré-conçu.
## Première partie : Gestion des fichiers
Afin de respecter une cohérence (et que le site puisse chercher les fichiers au bon endroit) dans les dossiers, voici comment doit être structuré les éléments que vous souhaitez ajouter :
Les pages en MarkDown (qui peuvent être aussi bien des fichiers comme "mapage.md" ou "monfichier.txt" (en gros le fichier doit soit être un document texte soit un document MarkDown (finissant par .md))) doivent être placées dans le dossier /pages
Les images doivent quand à elles être placées dans le dossier /static, elles peuvent être partout ça n'a pas d'importance, tant qu'elles sont dans ce dossier précisément. Si elles ne sont pas mises dans ce dossier, le site n'y aura pas accès ! Pour implémenter les images dans les pages, on verra plus bas comment faire

## Deuxième partie : Synthaxe
La synthaxe est très simple : tout d'abord sachez que vous ne pouvez pas (encore) mettre des items (des liens, images ect) au milieu de texte
Pour créer le titre de la page (nécessaire et UNIQUE) il suffit de commencer le fichier par un # suivi d'un espace, exemple "# Mon titre"
Vous pouvez créer des titres plus petits, il suffit de rajouter plusieurs # : par exemple "## Mon titre 2" sera plus petit que le titre de la page, et "### Mon titre 3" sera ENCORE plus petit. Vous pouvez pour l'instant jusqu'à la taille "##### Mon titre 5", qui sera vraiment tout petit (il peut être utile en remerciements de bas de page par exemple).

Vous pouvez également rajouter des liens et des images :
Pour ajouter des images, vous devez commencer votre ligne par "img:", le programme détectera alors une image. La suite devra être organisée sous cette forme : ":color:crimson::-```-img:[static/mon/lien/vers/l'image]{Ma description de l'image qui apparaitra en dessous}-:color-```". Il pourra également être un lien vers une autre page HTML (que je déconseille parce que si le site d'où vient l'image supprime l'image elle n'existera plus) : "img:[https://exemple.com/mon_image.png]{Mon sous-titre/description de l'image}"
Les liens peuvent être ajoutés de la même façon que les images, il suffit simplement de commencer la ligne par "link:" au lieu de "img:", exemple : "link:[https://exemple.com]{Texte affiché à la place du lien}"

## Troisième partie : Paragraphes et sauts de ligne
À la suite d'un titre, deux choix d'offrent à vous : sauter une ligne, ou ne pas sauter de ligne ? C'est au choix : Toutes les lignes que vous sautez laissera des espaces entre les texte, images et autre. Petits exemples :

Pour le paragraphe suivant je ne vais pas sauter de ligne, je vais juste retourner simplement à la ligne
Et voilà, j'ai un petit espace, maintenant je vais sauter une ligne :

Hop ! Un plus grand espace entre deux paragraphes ; il peut être utile pour changer de partie par exemple

## Quatrième partie : Mise en forme du texte
Récemment (après la présentation à l'oral) nous avons ajouté un système pour ajouter de l'italique, du gras ect. Encore une fois, nous avons essayé de vous faire un système le plus simple possible :
- Vous pouvez mettre **-du texte en gras-** en entourant le texte par "**/-" au début et par "-/**" à la fin, exemple : **/-Mon texte en gras-/**
- Vous pouvez mettre _-du texte en italique-_ en entourant le texte par "_/-" au début et par "-/_" à la fin, exemple : _/-Mon texte en italique-/_
- Vous pouvez ~~-barrer du texte-~~ en entourant le texte par "~~/-" au début et par "-/~~" à la fin, exemple : ~~/-Mon texte barré-/~~
- Vous pouvez mettre ```-du texte en monospace-``` en entourant le texte par "```/-" au début et par "-/```" à la fin, exemple : ```/-Mon texte en monospace-/```
- Vous pouvez mettre ^^-du texte en exposant-^^ en entourant le texte par "^^/-" au début et par "-/^^" à la fin, exemple : ^^/-Mon texte en exposant-/^^
- Et vous pouvez aussi ,,-mettre du texte en indice-,, en entourant le texte par ",,/-" au début et par "-/,,", exemple : ,,/-Mon texte en indice-/,,
- Vous pouvez ==-surligner du texte-== en entourant le texte par "==/-" au début et par "-/==" à la fin, exemple : ==/-Mon texte en surligné-/==
- Vous pouvez ++-souligner du texte-++ en entourant le texte par "++/-" au début et par "-/++" à la fin, exemple : ++/-Mon texte en souligné-/++

## Cinquième partie : Zone plus complexe
Voici quelques mises en forme que nous avons ajouté, mais qui sont plus complexes à utiliser (et à retenir, désolé):
Vous pouvez :color:blue::-mettre du texte en couleur-:color en entourant le texte par ":color/:couleur:/:-" en mettant votre couleur en anglais à la place de "couleur" au début et finir par "-:/color", exemple :color/:blue:/:-Mon texte en bleu-:/color et :color:red::-ici en rouge-:color
Il n'y a pas toutes les couleurs disponibles mais une très grande partie quand même. Si quand vous rechargez la page, votre texte ne change pas de couleur, alors la couleur que vous avez choisi n'est pas disponible.

Vous pouvez également "additionner" plusieurs mises en formes, quelques exemples : **- ==- ~~-Mon texte en gras, barré et surligné-== -~~ -** ou encore _-^^-Mon texte en italique et exposant-^^-_ : c'est assez complexe parce que parfois il faut respecter une certaine hiérarchie, mais en général ça marche dans n'importe quel sens. Par exemple le surlignage doit toujours être au plus proche du texte (avec le moins d'espaces possibles), il doit être comme cela : **/- ==/-Mon texte surligné-/== -/** et non pas comme cela : ==/- **/- Mon texte surligné -/** -/==
Autre information : il ne faut pas hésiter à mettre des espaces entre les mises en forme, par exemple : ```- **/- ==/- Mon texte surligné -/== -/** -```
Il peut être parfois nécessaire de faire plusieurs tests pour trouver la bonne composition
