<p align="center">
    <strong>Santa Cruz Island Spotted Skunk Project</strong>
</p>

 A ML workflow for identifying spotted skunks from camera trap images taken on Santa Cruz Island in California's Channel Islands
<p align="center">
    <img src="santa_cruz_island.jpeg" alt="santa cruz island" width="500">
</p>

## Background
On the Channel Islands there are many species of animals, some that are endemic and other that are not. One example of the an endemic species would be the island spotted skunk (Spilogale gracilis amphialus) is an insular endemic carnivore and a subspecies of the western spotted skunk (Spilogale gracilis). The skunk is only currently found on two islands off the southern coast of California (Santa Cruz Island, and Santa Rosa Island, where its occurrence is rare). Its presence has been recorded on San Miguel Island, but it has since been declared extinct in that area. The Channel Island skunk is one of two terrestrial carnivores on the islands, the other being the island fox. It is designated as a species of special concern by the state of California as its population has seen a regression in the recent years. For this reason the National Park Service, Smithsonian OCIO Data Science lab as well as the Smithsonain Scholars Program at UCSB have taken on the on going project of using machine learning & artificiall intelligence to help analyze the popluation and decide weather this species of special concern should be declared endangered or not. 

## Methods

As previously mentioned, since mid 2018 the National Park Service (NPS), Smithsonian Offie of Chief Information Officer (OCIO) Data Science Lab, and the UC, Santa Barbara Office Smithsonian Scholars have partnered together to analyze the spotted skunk poplution. On the Santa Rosa Island, we are using the Date/Time stamps on a number remote cameras which have been operating continuously from October 2018 to present to assess seasonal activity patterns of island spotted skunk and island fox. These cameras are motion activiated and are sensative to the motion of a motving branch, passing skunk or flying bird, ultamitly causing them to take thousands of pictures a day most of which are empty pictures. We however don't know which are empty and which are not so we must anylyze them one by taking up a lot of time and resources. For this reason we have decided to employ machine learning as to automate our workflow 

<p align="center">
    <img src="reconyx_hyperfire_camera.jpeg" alt="reconyx hyperfire camera" width="500">
</p>

### Data Mining Relavent Data

Since we have partner with the NPS and the Smithonian OCIO Data Science lab we have access to more than 240,000 annoted images located on the [
Labeled Information Library of Alexandria: Biology and Conservation (LILA BC)]([[/guides/content/editing-an-existing-page](https://www.section.io/engineering-education/understanding-coco-dataset/)](https://lila.science/datasets/channel-islands-camera-traps/)) which follow the [COCO Data Set format]([/guides/content/editing-an-existing-page](https://www.section.io/engineering-education/understanding-coco-dataset/)) as well acess to 2,500 annoted images annoted using stadard practice.  


### Tidy Data 

#### Renaming and Normalizing Data

As mentioned, images from the LILA BC data set were annoted using the COCO dataset format and were normalized using best practices which can be found in the ```Renaming_moving.ipynb``` file as well as the ```mass_move.sh```. In addition to this, we collected camera trap data. given that we are processing images from from over X_NUM cameras we are therefor receiving thousands of images everytime we go into the field. For this reason we must be  able to keep track of the images site number, camera number, expedition number, and other metadata that we must include as part of our preprocessing procedure. To do this in an fast effecient manner we created a shell script that takes in n vairables and renames the images that collected based on user input. 

```
mass_rename.sh
```
