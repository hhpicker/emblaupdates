# IMPORT STUFF

import tweepy
from credentials import *
import random
import os

############################################################################

def embla_updates(request):

	# Access and authorize our Twitter credentials from credentials.py

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)


	############################################################################


	#PROGRAM

	# Here is a list of phrases the bot can tweet out.
	phrases = [
		"screaming at Holly's door.", 
		"running around the house.", 
		"screaming at the door.",  
		"screaming at her food dish.", 
		"napping.", 
		"napping in her cat cave.", 
		"napping on the sofa.", 
		"napping on her cat tree.", 
		"chewing on electrical wires.", 
		"eating houseplants.", 
		"playing with her toy mouse.",
		"screaming at the cupboard 'MORE!! MOUSE!!'", 
		"lying outside Holly's door.", 
		"having a bath.", 
		"cleaning her toebeans.", 
		"screaming to be let inside.", 
		"screaming for cuddles.", 
		"cuddling.", 
		"using the litterbox.",
		"exploring the storage room.", 
		"hunting for mice.", 
		"scratching furniture.", 
		"scratching her cat tree.", 
		"trying to wrestle.", 
		"wrestling with Holly.", 
		"fighty.", 
		"acting goofy.", 
		"being an obsession bean.", 
		"trying to catch a fly.", 
		"trying to eat a fly.", 
		"sitting in a box.", 
		"camouflaged outside.", 
		"chasing the laser pointer.", 
		"eating some kibble.", 
		"eating wet food.", 
		"eating raw food.", 
		"sleeping.", 
		"purring a lot.", 
		"purring a little.", 
		"rubbing up against Holly's leg.", 
		"making dough.", 
		"cuddling with Dan.", 
		"jumping to the table.", 
		"sniffing everything she can get close to.", 
		"trying to chew on anything within sight.", 
		"biting.", 
		"biting the leather purse.", 
		"chewing on the cardboard box.", 
		"lying on the bed.", 
		"trying to eat gravel.", 
		"trying to eat the knitting needles.", 
		"not dealing with her oral fixation.", 
		"trying to get the bug.", 
		"trying to catch literally anything on Holly's desk.", 
		"batting at the fuzzy snake.", 
		"rubbing her face on anything she can get near to.", 
		"being petted.", 
		"being petted by two people at once.", 
		"drinking water.", 
		"trying to steal hair elastics.", 
		"trying to steal a sip of Holly's water.", 
		"trying to steal twist ties.", 
		"staring at you creepily.", 
		"accidentally scratching Holly.", 
		"meowing at the top of her lungs at 4am.", 
		"loving on her piece of honeysuckle.", 
		"trying to eat string.", 
		"causing her mom thousands of dollars in vet bills.", 
		"giving love eyes to her mom.", 
		"headbutting Holly.",
		"headbutting Dan.", 
		"yawning.", 
		"panting from playing.", 
		"perching on a shoulder.", 
		"lying like a koala on the back of the desk chair.", 
		"pretending she's in the jungle.",
		"watching birds.", 
		"watching birds on youtube.", 
		"getting in the way.", 
		"putting her butt in people's faces.", 
		"being a shithead.", 
		"being a goof.", 
		"going outside.", 
		"braving the snow.", 
		"frolicking in the grass.", 
		"hiding under the deck.", 
		"getting in a catfight.", 
		"hissing at the neighbour's cats.", 
		"eating the tips of the houseplants leaves off.", 
		"barfing up the houseplant leaves.", 
		"butt in face.",
		"having a mood swing.", 
		"trying to climb the screen door.", 
		"trying to attack the moths through the window.", 
		"getting her claws stuck in the screen.", 
		"trying to pull the screen off the window.", 
		"being bad and jumping on the counter.", 
		"sniffing human food and finding it not up to her standards.", 
		"giving Holly a mouse present.", 
		"trying to open the cupboard door without opposable thumbs and failing.", 
		"loving the printer.", 
		"attacking the printer.", 
		"being ridiculous.", 
		"trying to eat things that are not edible.", 
		"playing in grocery bags.", 
		"playing grocery bag games.", 
		"playing in boxes.", 
		"eating some salmon for her birthday.", 
		"thinking salmon is the best.", 
		"hiding in a blanket fort.", 
		"meowing at Holly's door.", 
		"waking everyone up at night.", 
		"having trouble with object permanence.", 
		"hoping that the weather might have changed in the 2 minutes since she tried to go outside.", 
		"hating every other cat in existence.", 
		"yelling at the neighbour's cat through their window.", 
		"knocking over Holly's mirror.", 
		"tearing up tissue paper.", 
		"eating ribbon.", 
		"causing her mom a heart attack.", 
		"living her best life all the time.", 
		"so hungry; she's never been fed in her entire life, not even once!", 
		"obsessing about mice.", 
		"obsessing about going outside.", 
		"obsessing about getting under Holly's bed.", 
		"trying futilely to get under Holly's bed.", 
		"scratching the box that's preventing her from getting under Holly's bed.", 
		"knocking things over and breaking them.", 
		"knocking instruments off their stands and breaking them.", 
		"trying to get at the velcro holder on the XLR cable.", 
		"trying to climb the shelves in the bathroom.", 
		"being 200 percent cat.", 
		"playing with a real mouse!",
		"lazing around.", 
		"being super annoying.", 
		"buttsnuggling Holly.", 
		"sleeping behind Holly on the chair.", 
		"digging her claws into the leather desk chair.", 
		"climbing the leather desk chair.", 
		"doing anything she can to get attention.", 
		"totally attention starved; no one has ever pet her even once.", 
		"galloping around the house.", 
		"stomp-walking.", 
		"being needy.", 
		"climbing a tree and isn't sure how to get down.",
		"on top of the shed.", 
		"perching on top of the railing outside.", 
		"being very friendly to strangers.", 
		"immediate best friends with anyone that gets invited over.", 
		"begging to be picked up.", 
		"curled up like a loaf of bread.", 
		"sleeping on the red chair."
	]

	# Here is a list of images the bot can tweet out.
	images = [
		"G:/Desktop/DH520/embla updates/embla.jpg", 
		"G:/Desktop/DH520/embla updates/embla1.jpg", 
		"G:/Desktop/DH520/embla updates/embla2.jpg", 
		"G:/Desktop/DH520/embla updates/embla3.jpg", 
		"G:/Desktop/DH520/embla updates/embla4.jpg", 
		"G:/Desktop/DH520/embla updates/embla5.jpg", 
		"G:/Desktop/DH520/embla updates/embla6.jpg", 
		"G:/Desktop/DH520/embla updates/embla7.jpg", 
		"G:/Desktop/DH520/embla updates/embla8.jpg", 
		"G:/Desktop/DH520/embla updates/embla9.jpg", 
		"G:/Desktop/DH520/embla updates/embla10.jpg", 
		"G:/Desktop/DH520/embla updates/embla11.jpg", 
		"G:/Desktop/DH520/embla updates/embla12.jpg", 
		"G:/Desktop/DH520/embla updates/embla13.jpg", 
		"G:/Desktop/DH520/embla updates/embla14.jpg", 
		"G:/Desktop/DH520/embla updates/embla15.jpg", 
		"G:/Desktop/DH520/embla updates/embla16.jpg", 
		"G:/Desktop/DH520/embla updates/embla17.jpg", 
		"G:/Desktop/DH520/embla updates/embla18.jpg", 
		"G:/Desktop/DH520/embla updates/embla19.jpg", 
		"G:/Desktop/DH520/embla updates/embla20.jpg", 
		"G:/Desktop/DH520/embla updates/embla21.jpg", 
		"G:/Desktop/DH520/embla updates/embla22.jpg", 
		"G:/Desktop/DH520/embla updates/embla23.jpg", 
		"G:/Desktop/DH520/embla updates/embla24.jpg", 
		"G:/Desktop/DH520/embla updates/embla25.jpg", 
		"G:/Desktop/DH520/embla updates/embla26.jpg", 
		"G:/Desktop/DH520/embla updates/embla27.jpg", 
		"G:/Desktop/DH520/embla updates/embla28.jpg", 
		"G:/Desktop/DH520/embla updates/embla29.jpg", 
		"G:/Desktop/DH520/embla updates/embla30.jpg", 
		"G:/Desktop/DH520/embla updates/embla31.jpg", 
		"G:/Desktop/DH520/embla updates/embla32.jpg", 
		"G:/Desktop/DH520/embla updates/embla33.jpg", 
		"G:/Desktop/DH520/embla updates/embla34.jpg", 
		"G:/Desktop/DH520/embla updates/embla35.jpg", 
		"G:/Desktop/DH520/embla updates/embla36.jpg", 
		"G:/Desktop/DH520/embla updates/embla37.jpg", 
		"G:/Desktop/DH520/embla updates/embla38.jpg", 
		"G:/Desktop/DH520/embla updates/embla39.jpg", 
		"G:/Desktop/DH520/embla updates/embla40.jpg", 
		"G:/Desktop/DH520/embla updates/embla41.jpg", 
		"G:/Desktop/DH520/embla updates/embla42.jpg", 
		"G:/Desktop/DH520/embla updates/embla43.jpg", 
		"G:/Desktop/DH520/embla updates/embla44.jpg", 
		"G:/Desktop/DH520/embla updates/embla45.jpg", 
		"G:/Desktop/DH520/embla updates/embla46.jpg", 
		"G:/Desktop/DH520/embla updates/embla47.jpg", 
		"G:/Desktop/DH520/embla updates/embla48.jpg", 
		"G:/Desktop/DH520/embla updates/embla49.jpg", 
		"G:/Desktop/DH520/embla updates/embla50.jpg", 
		"G:/Desktop/DH520/embla updates/embla51.jpg", 
		"G:/Desktop/DH520/embla updates/embla52.jpg", 
		"G:/Desktop/DH520/embla updates/embla53.jpg", 
		"G:/Desktop/DH520/embla updates/embla54.jpg", 
		"G:/Desktop/DH520/embla updates/embla55.jpg", 
		"G:/Desktop/DH520/embla updates/embla56.jpg", 
		"G:/Desktop/DH520/embla updates/embla57.jpg", 
		"G:/Desktop/DH520/embla updates/embla58.jpg", 
		"G:/Desktop/DH520/embla updates/embla59.jpg", 
		"G:/Desktop/DH520/embla updates/embla60.jpg"
	]

	# Choose both a phrase and an image
	phrase_selection = "Embla is " + random.choice(phrases)
	imagePath = random.choice(images)

	# This makes a pseudo-random choice between the phrase or the image, except the phrase is weighted to be chosen ten times as often as the image.
	# k = 1 refers to how many elements should be chosen.
	real_choice = random.choices([phrase_selection, imagePath], weights = [10, 1], k = 1)

	# This turns the real_choice list into a string, which is what the if/else statement below is expecting.
	real_real_choice = ''.join(real_choice)

	# If the random choice is an file/image, use the update_with_media command. If not, use the update_status command.
	try:
		if os.path.isfile(real_real_choice):
			api.update_with_media(imagePath)
			print('This tweets an image.')
			print(imagePath)
		else:
			api.update_status(phrase_selection)
			print('This tweets a phrase.')
			print(phrase_selection)
	except:
		print('An error occurred.')
		exit()