# ProjectWork
Our task was to build a tool such that it will be able to take the notes from the class for the student.Now when the student sees anything outside in the world,he is able to upload that photo to our tool.We shall be able to tell him about the application of the notes relating to that image.**Hence helping in better understanding of the real world applications of the material studied in the class**.


# First Step

Our First Task was to extract tags from the image.
For this we employed google reverse image search to help us.
We uploaded the image to the google reverse image search algorithm and extracted the search query it displayed.
**For example on uploading a image for rock concert we get the following result**:

![rock concert](https://github.com/mananmadan/ProjectWork/blob/master/rockconcert.jpg)
# Second Step

Now that we had the description of the image , we had to form different categories from that result.
So we decided to extract many levels of categories from wikipedia to ensure that we get may related field regarding the tag of the image.
After doing that we put all that information in a graph using google fusion tables.
**For example for query "food" and number of levels = 3 we get**:
![test](https://github.com/mananmadan/ProjectWork/blob/master/graph.jpg)
# Third Step

We take the tags from the notes and try to search the terms related to them first in wikipedia.
Then we try to relate any of these terms to the graph that contains the terms from the image categories.
We do the above process using the shortest path algorithm.
If the tag is found in the graph of pre-created graphs  ( image tag and the term which is related ) then we store it in a text file.
We do this for all pre-created graphs. The final text files has names of all the graphs that can be related to the image

# Fourth Step
## In Progress
In order to recommend the links to user, we first search the graph name and the image tag on google and select up to 10 URLs which are then sorted as per the occurrence of the two words. The criteria for the sort is that the URL in which the occurrence of both terms is maximum is recommended. For cases where occurrence of one term is greater but the other term is smaller , the URL in which minimum occurrence of the two words is greater is selected.
