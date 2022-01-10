#version 410

in vec3 position_eye, normal_eye, pt_pos;

uniform mat4 view_mat;

// fixed point light properties
vec3 light_position_world  = vec3 (0.0, 1.0, 0.0);
vec3 cameraDir = vec3 (0.0,0.0,1.0);
//object your working with is in y 1 plane

vec3 Ls = vec3 (1.0, 1.0, 1.0); // white specul0ar colour
vec3 Ld = vec3 (0.7, 0.7, 0.7); // dull white diffuse light colour
vec3 La = vec3 (0.2, 0.2, 0.2); // grey ambient colour

// stuff for spotlight
vec3 lightDir = vec3 (pt_pos- light_position_world);
float ang = 1.0; // this is in radians
float alha, CosAng, Costhet;
  
// surface reflectance
vec3 Ks = vec3 (1.0, 1.0, 1.0); // fully reflect specular light
vec3 Kd = vec3 (1.0, 0.5, 0.0); // orange diffuse surface reflectance
vec3 Ka = vec3 (1.0, 1.0, 1.0); // fully reflect ambient light
float specular_exponent = 10.0; // specular 'power'


out vec4 fragment_colour; // final colour of surface

void main () {
	//distance between light and point
	float dist = sqrt( (pt_pos[0]-light_position_world[0])*(pt_pos[0]-light_position_world[0]) + 
					   (pt_pos[1]-light_position_world[1])*(pt_pos[1]-light_position_world[1]) + 
					   (pt_pos[2]-light_position_world[2])*(pt_pos[2]-light_position_world[2]) );

	// ambient intensity
	vec3 Ia = (La * Ka);

	// diffuse intensity
	// raise light position to eye space
	vec3 light_position_eye = vec3 (view_mat * vec4 (light_position_world, 1.0));
	vec3 distance_to_light_eye = light_position_eye - position_eye;
	vec3 direction_to_light_eye = normalize (distance_to_light_eye);
	float dot_prod = dot (direction_to_light_eye, normal_eye);
	dot_prod = max (dot_prod, 0.0);
	vec3 Id = Ld * Kd * dot_prod; // final diffuse intensity

	
	// specular intensity
	vec3 surface_to_viewer_eye = normalize (-position_eye);
	
	// blinn
	vec3 half_way_eye = normalize (surface_to_viewer_eye + direction_to_light_eye);
	float dot_prod_specular = max (dot (half_way_eye, normal_eye), 0.0);
	float specular_factor = pow (dot_prod_specular, specular_exponent);
	
	vec3 Is = Ls * Ks * specular_factor; // final specular intensity

	//Compute V1 (pt_pos - light_position_world)
	vec3 v1 = vec3 (pt_pos[0] - light_position_world[0],pt_pos[1] - light_position_world[1],pt_pos[2] - light_position_world[2]);

	// get angle
	//CosAng = ((v1[0]*lightDir[0])+(v1[1]*lightDir[1])+(v1[2]*lightDir[2]))/sqrt((v1[0]*v1[0]+v1[1]*v1[1]+v1[2]*v1[2])*(lightDir[0]*lightDir[0]+lightDir[1]*lightDir[1]+lightDir[2]*lightDir[2])); //square and sqrt
	//alha = acos(CosAng); //is it in radians? 2 works.
	Costhet = (dot (lightDir,normal_eye))/ sqrt ((lightDir[0]*lightDir[0] + lightDir[1]*lightDir[1] + lightDir[2]*lightDir[2]));
	// final colour
		//fragment_colour = vec4(Is + Id + Ia, 1.0); //
	CosAng = (dot (cameraDir,normal_eye))/ (sqrt(cameraDir[0]*cameraDir[0] +cameraDir[1]*cameraDir[1]+ cameraDir[2]*cameraDir[2]));
	if (CosAng < (3.14/8)){ //border
		fragment_colour = vec4(0.1,0.1,0.1,1.0);
		}
	else{
		if (Costhet > 1.0){
		fragment_colour = vec4(Ia,1.0);
		}
		else if (Costhet > 0.5){
		fragment_colour = vec4(0.4,0.3,0.4,1.0);
		}
		else if (Costhet > 0.2){
		fragment_colour = vec4(0.7,0.6,0.7,1.0); 
		}
		else if (Costhet > 0.1){
		fragment_colour = vec4(0.8,0.7,0.6,1.0); 
		}
		else{
		fragment_colour = vec4 (0.9,0.8,0.8,1.0);
		}
		}
}