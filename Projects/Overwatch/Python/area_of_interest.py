# Intersection constants
I_CROP = (580, 250, 125, 45) # Use this for Image objects
IC_Y1, IC_Y2, IC_X1, IC_X2 = (I_CROP[1], I_CROP[1] + I_CROP[3], I_CROP[0], I_CROP[0]+I_CROP[2])  # Use this for VideoCapture frames
INTERSECTION_NAME = "_intersection.png"

# Road Left constants
RL_CROP = (26, 299, 50, 10)  # Use this for Image objects
RLC_Y1, RLC_Y2, RLC_X1, RLC_X2 = (RL_CROP[1], RL_CROP[1] + RL_CROP[3],
                                  RL_CROP[0], RL_CROP[0] + RL_CROP[2])  # Use this for VideoCapture frames
ROAD_LEFT_NAME = "_road_left.png"

# Road Left constants
RF_CROP = (6, 370, 50, 30)  # Use this for Image objects
RFC_Y1, RFC_Y2, RFC_X1, RFC_X2 = (RF_CROP[1], RF_CROP[1] + RF_CROP[3],
                                  RF_CROP[0], RF_CROP[0] + RF_CROP[2])  # Use this for VideoCapture frames
ROAD_FRONT_NAME = "_road_front.png"

# Misc Focus Area Constants
FOCUS_AREAS = [I_CROP, RL_CROP, RF_CROP]