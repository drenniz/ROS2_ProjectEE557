#Adding AprilTags

#An AprilTag is a PNG image applied as a texture to a thin box placed on a wall.

#1. Get the tag images. Use the tag36h11 family, which is the default for most ROS #detectors. The AprilRobotics apriltag-imgs repository on GitHub has ready-made PNGs. #Those files are tiny (about 10×10 pixels), so enlarge them with nearest-neighbor scaling #to around 800×800. Smooth scaling blurs the edges and breaks detection. Keep the white #border around the black square.
#https://github.com/AprilRobotics/apriltag-imgs

#2. Put the images in a folder Gazebo can find.

my_models/apriltags/model.config            (a minimal one, just a name)
my_models/apriltags/materials/textures/tag36h11_0.png
my_models/apriltags/materials/textures/tag36h11_1.png
bash
export GZ_SIM_RESOURCE_PATH=$HOME/my_models

#3. Add a tag box to the world file. This puts tag 0 on the inner face of the left outer #wall (that face is at x = −5.0), at 1.0 m height:

xml
<model name="tag_0">
  <static>true</static>
  <pose>-4.995 0 1.0 0 0 0</pose>
  <link name="link">
    <visual name="v">
      <geometry><box><size>0.01 0.3 0.3</size></box></geometry>
      <material>
        <diffuse>1 1 1 1</diffuse>
        <specular>0 0 0 1</specular>
        <pbr><metal>
          <albedo_map>model://apriltags/materials/textures/tag36h11_0.png</albedo_map>
          <roughness>1.0</roughness>
          <metalness>0.0</metalness>
        </metal></pbr>
      </material>
    </visual>
  </link>
</model>

#The box is 0.01 m thick and sits 0.005 m off the wall, which prevents flicker where the #two surfaces would overlap. For a wall face that points along ±y, swap the size to 0.3 #0.01 0.3 and offset the y position instead.

#Things to check
#Mirroring: compare the tag in Gazebo with your PNG. A mirrored tag will not be detected, #so if it looks flipped, flip the PNG left-to-right and reload.
#Tag size for the detector: the detector’s tag-size setting is the edge length of the #black square. If your image includes the white border, that is smaller than the box #width. A 10×10 image with a 1-pixel border gives a black square at 0.8 × the box width, #so a 0.3 m box has a 0.24 m tag.
#Height: put the tags at your robot camera’s height so they are in view.
#Moving tags: to put a tag on the spinner, add the same <visual> to the spinner’s bar link #and it will rotate with it.
#Texture not loading: if a tag shows up plain white or gray, the texture path isn’t #resolving. Check the -v4 log for a missing-file messag
