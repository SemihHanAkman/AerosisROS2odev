import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import random

class RastgeleDiziYayinlayici(Node):

    def __init__(self):
        super().__init__('rastgele_dizi_yayinlayici')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'raw_array', 10)
        self.timer = self.create_timer(1, self.rastgele_dizi_yayinla)

    def rastgele_dizi_yayinla(self):
        msg = Int32MultiArray()
        rastgele_dizi = [random.randint(0, 100) for _ in range(5)]  # 5 sayıdan oluşan dizi
        msg.data = rastgele_dizi
        
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayımlanan dizi: {rastgele_dizi}')

def main(args=None):
    rclpy.init(args=args)
    node = RastgeleDiziYayinlayici()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

