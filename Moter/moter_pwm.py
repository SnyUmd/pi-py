import pigpio
import time
import os

pin_pwm = 19
frq = 1000
duty = 50
pwm_duty = duty * 10000

pin_sw_in = 26

pi = pigpio.pi()

os.system('bash jtalk.sh "  タクトスイッチによりモータを制御いたします。"')


def main():
    #pin18 = 18

    pi.set_mode(pin_pwm, pigpio.OUTPUT)
    #pi.hardware_PWM(pin_pwm, frq,100)
    pi.write(pin_pwm, 1)

    pi.set_mode(pin_sw_in, pigpio.INPUT)
    pi.set_pull_up_down(pin_sw_in, pigpio.PUD_UP)

    cb0 = pi.callback(pin_sw_in, pigpio.FALLING_EDGE, cb_interrupt_f)
    cb1 = pi.callback(pin_sw_in, pigpio.RISING_EDGE, cb_interrupt_r)
    while True:
        test = 0

#立ち下がりの割り込み処理
def cb_interrupt_f(gpio, level, tick):
    os.system('bash jtalk.sh "モーターを回転させます。"')
    pi.hardware_PWM(pin_pwm, frq, pwm_duty)
    do_moter = True

        
    
#立ち上がり時の割り込み処理
def cb_interrupt_r(gpio, level, tick):
    os.system('bash jtalk.sh "モーターを停止させます。"')
    pi.write(pin_pwm, 1)

if __name__ == "__main__":
    main()

