import numpy as np
from scipy.optimize import minimize

class HexagonalSoundLocator:
    def __init__(self, radius):
        self.radius = radius
        self.microphone_positions = self._calculate_microphone_positions()
        self.sound_speed = 343

    def _calculate_microphone_positions(self):
        angles = np.linspace(0, 2*np.pi, 6, endpoint=False)
        x = self.radius * np.cos(angles)
        y = self.radius * np.sin(angles)
        return np.column_stack((x, y))

    def _objective_function(self, params, time_differences):
        x, y = params
        calculated_distances = np.linalg.norm(self.microphone_positions - [x, y], axis=1)
        calculated_time_diffs = calculated_distances / self.sound_speed - calculated_distances[0] / self.sound_speed
        return np.sum((calculated_time_diffs - time_differences)**2)

    def locate_sound_source(self, time_differences):
        initial_guess = [self.radius, self.radius]
        result = minimize(self._objective_function, initial_guess, args=(time_differences,), method='Nelder-Mead')
        x, y = result.x
        theta = np.arctan2(y, x)
        return x, y, theta

def main():
    radius = float(input("Enter radius: "))
    locator = HexagonalSoundLocator(radius)

    print("\nIntersection Points:")
    for point in locator.microphone_positions:
        print(f"({point[0]:.1f}, {point[1]:.10f})")

    time_differences = []
    for i in range(6):
        time = float(input(f"\nEnter time taken to reach microphone {i+1}: "))
        time_differences.append(time)
    time_differences = np.array(time_differences) - time_differences[0]
    x, y, theta = locator.locate_sound_source(time_differences)
    theta = theta % (2 * np.pi)
    print(f"\nEstimated Location of Sound Source: x = {x:.4f}, y = {y:.4f}")
    print(f"Estimated angle theta = {theta:.4f} radians")
    print(f"Estimated angle degrees = {np.degrees(theta):.4f} degrees")

if __name__ == "__main__":
    main()