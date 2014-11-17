//File: minha_correcao.c
//Purpose: 

//it's good for the program don't use global variables.
const unsigned int pingSensor_IO_pin = 7; 


//function that initilize variables. OBS.: this variables aren't being used in this program.
void setup(){
	
	int baudrate = 9600; 
	Serial.begin(baudrate);
}


/*
function that clean signal for first use and/or writes clean signal for the pulse.
variables: delayMicroseconds_low_state - int, time delay to clean signal of the pulse, in 2 microseconds
*/
void low_state(){
	
	pinMode(pingSensor_IO_pin, OUTPUT);
	digitalWrite(pingSensor_IO_pin, LOW); //clean signal
	const delayMicroseconds_low_state = 2;
	delayMicroseconds(delayMicroseconds_low_state);
}


/*
function that expressed the pulse on high state.
variables: delayMicroseconds_high_state - int, time delay to expressed signal of the pulse in high state, in 5 microseconds
*/
void high_state(){

	digitalWrite(pingSensor_IO_pin, HIGH);// <label id = "code.input.start_send_chirp"/>
	const delayMicroseconds_high_state = 5;	
	delayMicroseconds(delayMicroseconds_high_state);
	pinMode(pingSensor_IO_pin, INPUT);

}


/*
function that expressed the pulse on high state.
variables: duration_signal - 
*/
void read_duration_signal(){
	
	duration_signal = pulseIn(pingSensor_IO_pin, HIGH);// <label id = "code.input.read_duration"/>
	if(duration_signal>1) {
		const time_delay_duration = 50;		
		delay(time_delay_duration);
	}

	assert(duration_signal != NULL);	
	if(duration==0){

		Serial.println(Warning: We did not get pulse from sensor);
		Serial.print("Distance to nearest object");
		Serial.print(microseconds_to_cm(duration_signal));
		Serial.println("cm");
	}
}

long microseconds_to_cm(int microseconds){
	
	const unsigned delay_microseconds_to_cm = 100;	
	delay(delay_microseconds_to_cm);
	return microseconds/29/2;
}	




/* Function to call the other functions of this file
  
   @param pino - int, refers to the pino of arduino
   @param begin - boolean, refers to the begining of the pulse. This parameter is not being used
   Variable: delay_loop - int, refers to the delay of the loop with 100 miliseconds
  */
void loop(int pino, boolean begin){

	unsigned long duration;
	
	//chamar low_state pra limpar sinal
	//chamar high_state
	//chamar low_state
	//chamar read_duration

	delay(100);
}


