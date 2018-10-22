// PoVRay 3.7 Scene File " ... .pov"
// author:  ...
// date:    ...
//--------------------------------------------------------------------------
#version 3.7;
global_settings{ assumed_gamma 1.0 }
#default{ finish{ ambient 0.1 diffuse 0.9 }} 
//--------------------------------------------------------------------------
#include "colors.inc"
#include "textures.inc"
#include "glass.inc"
#include "metals.inc"
#include "golds.inc"
#include "stones.inc"
#include "woods.inc"
#include "shapes.inc"
#include "shapes2.inc"
#include "functions.inc"
#include "math.inc"
#include "transforms.inc"
#include "shapes3.inc"
//--------------------------------------------------------------------------
// camera ------------------------------------------------------------------
#declare Camera_0 = camera {/*ultra_wide_angle*/ angle 75      // front view
                            location <0.0, 1.0, -3.0>
                            right     x*image_width/image_height
                            look_at   <0.0 , 0.0 , 0.0>}
camera{Camera_0}
// sun ---------------------------------------------------------------------
light_source{< -3000, 3000, -3000> color White}
// sky ---------------------------------------------------------------------
sky_sphere { pigment { color rgb <0,0,0>} 
          
           } //end of skysphere

//--------------------------------------------------------------------------
//---------------------------- objects in scene ----------------------------
//--------------------------------------------------------------------------
union{
superellipsoid{ <2.50,2.50> 

     pigment{ color rgb<1,0.2,0.35> }
              finish { phong 1 }

     scale <.15,.15,.15> 
     rotate<0,0,0> 
     translate<0.2,0.2,0.1>
   }

difference{
superellipsoid{ <2.50,2.50> 

pigment{ color rgb<1,0.2,0.35> }
              finish { phong 1 }

     scale <.15,.15,.15> 
     rotate<0,0,0> 
     translate<0.2,0.2,0.1>
   }

superellipsoid{ <2.50,2.50>
color rgb<5,45,255> }
              finish { phong 1 }

     scale <.15,.15,.15> 
     rotate<0,0,0> 
     translate<0.2,-.05,0.1>
   }

}


 // ------------- end superellipsoid
 //----------------------------------------------------------------------------------------- 

//-----------------------------------------------------------------------------------------
object{ Round_Pyramid_N_in( // defined by incircle radii 
                            5 , // number of side faces 
                            <0,00,0>, 1.00, <0,1.25,0>, 0.00 , // A, radius A, B, radius_B, 
                            0.05, // wire radius or border radius 
                            0,   // 1 = filled, 0 = wireframe
                            0   // 0 = union, 1 = merge for transparent materials           
                          ) //-------------------------------------------------------------

pigment{ color rgb< 1.0 ,0.8, 0.1 >}
               //normal { bumps 0.5 scale 0.015}
                 finish { phong 1}


         scale <.75,.75,.75>*1 
         rotate <0,0,0>
         translate< .25, 0, 0>
       } // end of object -----------------------------------------------------------------   
//----------------------------------------------------------------------------------------- 

//---------------------------------------------------------------------------------------------- 
object{ Round_Pyramid_N_out( // definded by circumcircle radii
                             5 , // number of side faces 
                             <0,00,0>, 1.20, <0,0.8,0>, 0.40, // A, radius at A, B, radius at B, 
                             0.035, // wire radius or border radius 
                             0,  // 1 = filled, 0 = wireframe
                             0   // 0 = union, 1 = merge for transparent materials         
                           ) //-----------------------------------------------------------------
pigment{ rgb  <1, 1, 1 > }    
                   finish { phong 1 } 
  
 
         scale <1,1,1>*1 
         rotate <0,0,0>
         translate< .25, 0, 0>
       } // end of object//--------------------------------------------------------------------- 
//---------------------------------------------------------------------------------------------- 
