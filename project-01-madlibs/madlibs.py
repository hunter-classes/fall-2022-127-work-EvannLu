import random

heroes = ['Napoleon', 'Shakespeare', 'Da Vinci', 'Htiler', 'Aristotle', 'Jesus', 'Lincoln']
nouns = ['cow', 'kitty', 'secretary', 'rock', 'lion', 'cave', 'zookeeper', 'fish', 'bear', 'zebra']
verbs = ['run', 'dance', 'slide', 'jump', 'think', 'stand', 'smile', 'listen', 'eat', 'kill', 'run', 'punch', 'duck', 'scream']
adjectives = ['attractive', 'dazzling', 'elegant', 'shapely', 'gorgeous', 'apathetic', 'resolute', 'honorable', 'unnatural', 'young', 'severe']
adverbs = ['abnormally', 'absentmindedly', 'accidentally', 'adventurously', 'anxiously', 'arrogantly', 'awkwardly', 'bashfully']
heroes = random.choice(heroes)

f = open('story.txt', 'r')
storyD = f.read()