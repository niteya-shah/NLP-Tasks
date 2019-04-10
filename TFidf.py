from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dataset = [
"""
If there is a phrase I would prefer to retire
from online bios, personal or professional
it is, "I love travel." Or some approximation
of that sentiment. To clarify I am not
against travellers or those who proudly flaunt
their passion for travel. On the contrary,
editing a travel magazine has now made me
oddly protective of travellers and their ilk. My
submission is that "love to travel," suggested
so casually, just doesn't feel adequate to the
depth of emotion it sparks in true devotees."""
# In February, the month of love as endowed
# by our great gifting industrial complex, we
# are wrestling with what "love for travel"
# means in tangible, life-affecting terms. The
# early throes of discovering travel might not be
# too dissimilar to the beginnings of a feverish
# affair. A fleeting scene, sound or feeling that
# at first arouses, then enchants and eventually
# lures us into a hypnotic state, evoking woolly
# eyed reveries about what could be.
# This world, however, is not the most
# conducive for long-term passion, the kind
# that demands unflinching sustenance in
# the midst of distractions from a thousand
# notifications. Passion has many rivals to
# contend with. And in flippantly announcing
# travel as our first love, we are not fully
# considering the influence our other
# paramours (work , relationships or money) exert on us.
# """
,
"""One of the finer books I read this
year was John Kaag Hiking
With Nietzsche, in which Kaag
a professor of philosophy,
rekindles his passion for the German thinker
while tracing picturesque hiking trails in
the mountains of Switzerland. It's a near
precise rendering of the travelogue as a
self-help book. A young Kaag was an avowed
Nietzsche acolyte but given the ravages of
responsibilities and adulthood, the writer put
his affinity to test by undertaking physically
enduring hikes through the Alps, revisiting
haunts that the philosopher escaped to, in
search of solitude and salve. The journey's
demands, coupled with his own inner turmoil,
are catnip for anybody feeling at cross
purposes with their own life"""
#
# In the book, Kaag quotes Nietzsche writing
# to his mother after he had spent time in
# Splügen, "I was overcome by the desire to
# remain here... this high alpine valley... There
# are pure, strong gusts of air, hills and boulders
# of all shapes... But what pleases me the most
# are the splendid highroads over which I walk
# for hours." Travel as the answer to searching
# questions is hardly a radical idea but what's
# endearing about the book is that it subtly
# confirms a basic tenet of why we go on these
# journeys in the first place. Sometimes, being on the
# move matters more than anything else.
,
 """
 Summer is a charming flirt. Easy
 going and casual. Summer doesn't
 huff and puff to win our affections.
 It has us at "Hello." Winter broods
 like the tortured protagonist of big fat Russian
 novel. It is daunting and dramatic, burning
 with a slow intensity.

 The season's reputation precedes itself,
 and often, not in a good way. It has a way of
 whittling down everything to its bare bones.
 Even relationships not attuned to its ebbs
 and flows can fray. At a dinner conversation
 once attended, I listened in bemusement as
 a recent divorcee made the case that it was
 the Scandinavian frost that had cooled his
 ex-wife's ardour. How original."""

 # Winter travel is an exercise in negotiation,
 # especially for sunshine souls. "How many
 # extra clothes do I have to pack now?" "The
 # weather is minus-what-did-you-say?" All
 # valid concerns but the recommendations far
 # outweigh them. Take one trivial scoring point:
 # the winter wardrobe, which is tres chic, and
 # can make the most sartorially challenged
 # among us look like runway models.
 #
 # The allure of winter lies in nature-so
 # immense, overwhelming and, of course,
 # achingly beautiful. In his collection of letters
 # to an unborn daughter, Norwegian Karl Ove
 # Knausgård meditates on the sounds of the season.
 ]
for i in range(len(dataset)):
    dataset[i] = dataset[i].replace('\n'," ")
    dataset[i] = dataset[i].replace('\t'," ")

vectorizer = TfidfVectorizer()
val = vectorizer.fit_transform(dataset)
cosine_similarity(val[1],val[2])
