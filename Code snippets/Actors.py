#In Gazebo Harmonic, a scripted moving object is an actor: a model that follows a list of timed waypoints. Each moving obstacle has three settings:

#Asset: a walking skin for the person, and plain box visuals (or a mesh) for the forklift.
#Position: the <pose> of the actor, which is where it starts.
#Pattern: the waypoints. Each one has a time and a pose relative to the start, so speed is distance divided by time.

#Actors are not affected by physics, so they don’t collide with your robot or get pushed by it. Cameras can see them and GPU-based sensors such as lidar and depth cameras detect their meshes. That works for testing stop-and-yield behavior, since the robot has to avoid them on its own.

#Paste these blocks inside <world> in maze_world.sdf. I haven’t run them in Gazebo. The coordinates are chosen to fit your maze.

#Person: walks through the right doorway and back

#The walking skin downloads from Gazebo Fuel the first time you run it, so you need internet access once.

<actor name="person_1">
  <pose>3.4 -4.0 0 0 0 0</pose>
  <skin>
    <filename>https://fuel.gazebosim.org/1.0/Mingfei/models/actor/tip/files/meshes/walk.dae</filename>
    <scale>1.0</scale>
  </skin>
  <animation name="walk">
    <filename>https://fuel.gazebosim.org/1.0/Mingfei/models/actor/tip/files/meshes/walk.dae</filename>
    <interpolate_x>true</interpolate_x>
  </animation>
  <script>
    <loop>true</loop>
    <delay_start>0</delay_start>
    <auto_start>true</auto_start>
    <trajectory id="0" type="walk" tension="1.0">
      <waypoint><time>0</time>  <pose>0 0  1.0 0 0  1.5708</pose></waypoint>
      <waypoint><time>12</time> <pose>0 12 1.0 0 0  1.5708</pose></waypoint>
      <waypoint><time>13</time> <pose>0 12 1.0 0 0 -1.5708</pose></waypoint>
      <waypoint><time>25</time> <pose>0 0  1.0 0 0 -1.5708</pose></waypoint>
      <waypoint><time>26</time> <pose>0 0  1.0 0 0  1.5708</pose></waypoint>
    </trajectory>
  </script>
</actor>

#The type="walk" on the trajectory must match the animation’s name="walk". A tension of 1.0 keeps the path close to your waypoints, because the default can overshoot them. If the person walks sideways, add or subtract 1.5708 from the yaw values.

#Forklift: shuttles along the lane below the left doorway

#This one has no skin. It’s a body of box visuals that the trajectory carries around. It goes forward, pauses, then reverses without turning, so its heading differs from its direction of travel. That is a good test for a robot that checks which way the forklift is moving.

<actor name="forklift_1">
  <pose>-3.5 -3.3 0 0 0 0</pose>
  <link name="body">
    <visual name="chassis"><pose>0 0 0.5 0 0 0</pose>
      <geometry><box><size>1.8 1.1 0.8</size></box></geometry></visual>
    <visual name="mast"><pose>1.0 0 1.0 0 0 0</pose>
      <geometry><box><size>0.12 0.9 2.0</size></box></geometry></visual>
    <visual name="fork_left"><pose>1.6 0.3 0.1 0 0 0</pose>
      <geometry><box><size>1.0 0.12 0.05</size></box></geometry></visual>
    <visual name="fork_right"><pose>1.6 -0.3 0.1 0 0 0</pose>
      <geometry><box><size>1.0 0.12 0.05</size></box></geometry></visual>
  </link>
  <script>
    <loop>true</loop>
    <delay_start>0</delay_start>
    <auto_start>true</auto_start>
    <trajectory id="0" type="shuttle" tension="1.0">
      <waypoint><time>0</time>  <pose>0   0 0 0 0 0</pose></waypoint>
      <waypoint><time>5</time>  <pose>3.5 0 0 0 0 0</pose></waypoint>
      <waypoint><time>7</time>  <pose>3.5 0 0 0 0 0</pose></waypoint>
      <waypoint><time>12</time> <pose>0   0 0 0 0 0</pose></waypoint>
      <waypoint><time>14</time> <pose>0   0 0 0 0 0</pose></waypoint>
    </trajectory>
  </script>
</actor>

#For a nicer asset, search for “forklift” at app.gazebosim.org/fuel/models and use its mesh URI in a <visual>, or paste the <include> snippet it gives you. I couldn’t confirm a specific forklift model there.

#To change a pattern, edit the waypoints. A square route is four corners, and a one-time crossing is loop false. To stagger several actors, give each a different delay_start. That delay is waited before every cycle when looping. To add more, copy a block, rename it, and change its pose and waypoints.

#If you need the forklift to collide physically, there are two other routes:

#The TrajectoryFollower plugin drives a real model through waypoints with force and torque.
#A drivable model that you command with /cmd_vel needs the ROS bridge: sudo apt install ros-jazzy-ros-gz.

