import wpilib
ARM_DOWN = 1
DRIVE = 2
ARM_UP = 3
class PortcullisLift:
 
    def __init__(self, drive, intake, drive_speed=-.2):
        self.intake = intake
        self.drive = drive
        
        self.drive_speed = drive_speed
        
        self.is_running = False
        self.state = ARM_DOWN
        
        self.timer = wpilib.Timer()
    def get_running(self):
        return self.is_running
    
    
    def doit(self):
        self.is_running = True
        #Add state machine to put the arm at the bottom first
        if self.state == ARM_DOWN:
            self.intake.set_arm_bottom()
            if self.intake.on_target():
                self.timer.reset()
                self.state = DRIVE
        if self.state == DRIVE:
            self.drive.move(self.drive_speed, 0)
            if self.timer.hasPeriodPassed(1):
                self.state = ARM_UP
        if self.state == ARM_UP:
            self.intake.set_arm_top()
            if self.intake.on_target():
                self.is_running = False
        
    