How does a robot in slam work?

    Which algorithm to explore map?
        Bug, sampling based, quad tree?
    
    Bredth first or depth first?
    
    April tag target
        Use dyjkstras algorithm for shortest path routing
        
    Goal if there is an objective highest priority
    if not found explore
    
    Set boundaries 
    
    Account for algorithm?
    
    Recorded oputput?
    
    Output certainty of lacation?
    
    If distance to object is=>0 stop for time x and alarm1
        Back away from obsticle resume path
        
    If battery is <15% return to docking station
    If battery <5% and docking station is not reachedd find closset goal tag and alarm2
    
    If there is no goal or goal has not been located explore map
    
    If existing map exists use it to localize and find goal location
        use it to re sample
        AMCL
    If goal is present find fastes path to goal
    
    If object is moving set to actor
        If actor <10 m slow down
        if actor <2 m stop
        if actor <1 m move away
            
    if all goals are explored and path value <x find goal location and wait
        else locate goal and map and localize.
    If time 18:00<5:00 move to dock
    
    If no path is found retry after 30s and add error tick
        if error tick =5 enter relocalization
        
    
    If no lcalizationi s found retry after 30s and add error tick
         if error tick =5 enter relocalization
         
    If path is know plan tragectroy 
    
