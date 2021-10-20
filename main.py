from translate import Translator

translator = Translator(to_lang="Hindi")

translation = translator.translate('hello!')
print(translation)