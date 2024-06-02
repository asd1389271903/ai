#由chatgpt輔助
import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
observation, info = env.reset(seed=42)

durations = []

for episode in range(10):  
    observation, info = env.reset()
    duration = 0
    while True:
        env.render()
        cart_pos, cart_vel, pole_angle, pole_ang_vel = observation
        
        if pole_angle < 0 and pole_ang_vel < 0:
            action = 0  
        elif pole_angle > 0 and pole_ang_vel > 0:
            action = 1   
        else:
            action = 0 if pole_angle < 0 else 1  
        
        observation, reward, terminated, truncated, info = env.step(action)
        duration += 1
        
        if terminated or truncated:
            durations.append(duration)
            print(f'Episode {episode + 1} finished after {duration} timesteps')
            break

env.close()

print('Durations:', durations)