import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class DiziDinleyici(Node):

    def __init__(self):
        super().__init__('dizi_dinleyici')
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'raw_array',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        alinan_dizi = msg.data
        toplam = sum(alinan_dizi)  # Dizinin toplamı
        cift_sayilar = [num for num in alinan_dizi if num % 2 == 0]
        cift_sayi_sayisi = len(cift_sayilar)  # Çift sayıların sayısı
        
        self.get_logger().info(f'Alınan dizinin toplamı: {toplam}, Çift sayı adedi: {cift_sayi_sayisi}')

def main(args=None):
    rclpy.init(args=args)
    node = DiziDinleyici()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

