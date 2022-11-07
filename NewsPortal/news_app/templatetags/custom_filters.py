from django import template

register = template.Library()

@register.filter()
def censor(value):
	stop_list_words = ['сосала', 'валят']
	for word in value.split():
		if word.lower() in stop_list_words:
			value = value.replace(word, f'{word[0]}{"*" * (len(word)-1)}')
	return value
