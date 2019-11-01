# ProjectWork
Introductory line


# First Step

Our First Task was to extract tags from the image.
For this we employed google reverse image search to help us.
We uploaded the image to the google reverse image search algorithm and extracted the search query it displayed

# Second Step

Now that we had the description of the image , we had to form different categories from that result.
So we decided to extract many levels of categories from wikipedia to ensure that we get may related field regarding the tag of the image.
After doing that we put all that information in a graph.

![test]()
# Third Step

We take the tags from the notes and try to search the terms related to them first in wikipedia.
Then we try to relate any of these terms to the graph that contains the terms from the image categories.
We do the above process using the shortest path algorithm.
No we calculate weight of each technical term(obtained from the notes) related to the terms in the image.
We order them according to their weights.

# Fourth Step 
 In order to recommend the links to user , we desighn a search query of the tags that had the most weight and then display them.
