# Multilingual detection

The aim of this program is to recognize different languages in a multilingual text.

This Python project uses [NLTK](https://www.nltk.org/) for tokenization and [Fasttext](https://fasttext.cc/) for language detection.

## Prerequisites
- Python > 3.8
- [NLTK library](https://www.nltk.org/)
- [Fasttext library](https://fasttext.cc/docs/en/python-module.html)
- Fasttext pre-trained model:
    - [lid.176.bin](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin): complete model (126MB)
    - [lid.176.ftz](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz): compressed version (917kB)

## Usage

### Command line
Use the following command line by changing the different parameters:

```sh
python fasttext_model_path txt_file_path json_output_path
```

### Parameters
- ```fasttext_model_path```: path to Fasttext pre-trained model
- ```txt_file_path```: input, path to the txt file to analyze
- ```json_output_path```: output, json document which contains the different pieces of text, their language along with the confidence index granted by Fasttext

### Configuration

The tokenizer used in this program (NLTK Punkt) has been altered in order to keep unchanged the formatting (i.e., line breaks).      

Line breaks in json files are represented by "\n". If you want to remove those, change the parameter ```line_break=True``` line 100 of the Python file by ```line_break=False```.

### Example
You can use the data example provided to test the program:
```sh
python model/lid.176.bin data/data_example.txt results/result_example.json
```

The data example  was built from different languages of wikipedia entries of [*Celeste* (video game)](https://en.wikipedia.org/wiki/Celeste_(video_game))

### Output

The output of this program is a json file with the following arguments and values:
- **"text"**: source text
- **"lang"**: language ISO code (see ISO [639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes))
- **"confidence"**: Fasttext's confidence index for the given language (score between 0 and 1, rounded to 4 decimals)

```xml
[
{
"text": "Celeste est un jeu vidéo indépendant de plateformes en deux dimensions développé et édité par Extremely OK Games, un studio canadien dirigé par Maddy Thorson et Noel Berry. Issu d'un prototype éponyme développé en août 2015 lors d'une game jam sur la fantasy console PICO-8, il est finalement publié sur Microsoft Windows, macOS, Linux, PlayStation 4, Nintendo Switch et Xbox One le 25 janvier 2018, puis sur Google Stadia le 28 juillet de la même année.\n Dans Celeste, le joueur incarne Madeline, une jeune femme qui tente de gravir le mont Celeste.",
"lang": "fr",
"confidence": 0.9838
},
{
"text": "During her ascent, it is revealed that she suffers from a severe form of anxiety and depression, implying that she has to face her anxieties and inner malaise to reach the top of the mountain.",
"lang": "en",
"confidence": 0.9919
},
{
"text": "Le jeu est composé de huit chapitres ainsi que d'un DLC gratuit intitulé Farewell, sorti le 9 septembre 2019, qui clôt définitivement l'histoire. Le gameplay du jeu consiste en une suite d'écrans présentant un assemblage complexe et cohérent d'obstacles qui demandent à la fois de la stratégie, de la précision et un bon temps de réaction de la part du joueur pour être surmontés.",
"lang": "fr",
"confidence": 0.9998
},
{
"text": "Az igényesnek tartott és gyakran a Super Meat Boyhoz hasonló játékokhoz hasonlított Celeste mindazonáltal tartalmaz beállításokat a nehézség beállítására, és kevésbé büntetőnek tekinthető, mint a műfaj többi játéka.\n",
"lang": "hu",
"confidence": 0.9956
},
{
"text": "Celeste est très bien reçu par la critique et est loué pour ses mécaniques de jeu, son level design, sa musique — composée par Lena Raine —, son esthétique graphique 8 bits et son histoire, en particulier pour le travail effectué sur le personnage de Madeline ainsi que sur celui de représentation des troubles psychiques.",
"lang": "fr",
"confidence": 0.9994
},
{
"text": "它被行业媒体认为是2018年最好的游戏之一，赢得了许多奖项，包括2018年游戏奖的最佳独立游戏和同一仪式的年度游戏提名。",
"lang": "zh",
"confidence": 0.9953
},
{
"text": "Il s'agit en outre d'un succès commercial, Celeste s'étant écoulé à plus d'un million d'exemplaires en mars 2020, tout en devenant très populaire dans la communauté du speedrun.",
"lang": "fr",
"confidence": 0.9953
}
]
```
