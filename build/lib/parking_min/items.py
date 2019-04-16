# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ParkingMinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Headline(scrapy.Item):
    """
    ニュースのヘッドラインを表すItem。
    """
    url = scrapy.Field()
    生産国_country = scrapy.Field()
    メーカー_maker = scrapy.Field()
    ジャンル_genre = scrapy.Field()
    モデル名_model_name = scrapy.Field()
    グレード名_model_grade = scrapy.Field()
    新車価格_new_car_price = scrapy.Field() #新車価格
    発売日_release_date = scrapy.Field() #発売日
    発売区分_release_category = scrapy.Field() #発売区分
    新車販売状況_new_car_sales_situation = scrapy.Field() #新車販売状況
    型式_model_number = scrapy.Field() #型式
    動力分類_power_classification = scrapy.Field() #動力分類
    駆動方式_drive_system = scrapy.Field() #駆動方式
    ハンドル位置_handle_position = scrapy.Field() #ハンドル位置
    乗車定員_boarding_capacity = scrapy.Field() # 乗車定員
    ドア数_number_of_doors = scrapy.Field() # ドア数
    シート列数_number_of_sheet_columns = scrapy.Field() # シート列数
    車両重量_vehicle_weight = scrapy.Field() # 車両重量
    車両総重量_vehicle_gross_weight = scrapy.Field() # 車両総重量
    排気量_displacement = scrapy.Field() # 排気量
    
    最高出力_kw_highest_output = scrapy.Field() # 最高出力
    最高出力_ps_highest_output = scrapy.Field() # 最高出力
    最高トルク_nm_maximum_torque = scrapy.Field() # 最高トルク
    最高トルク_kgfm_maximum_torque = scrapy.Field() # 最高トルク
    
    過給機_turbocharger = scrapy.Field() # 過給機
    アイドリングストップ_idling_stop = scrapy.Field() # アイドリングストップ
    燃料_fuel = scrapy.Field() # 燃料
    燃料タンク容量_fuel_tank_capacity = scrapy.Field() # 燃料タンク容量
    総電力量_total_power = scrapy.Field() # 総電力量
    充電走行距離_charging_distance = scrapy.Field() # 充電走行距離
    
    モーター最高出力_kw_motor_highest_output = scrapy.Field() # モーター最高出力
    モーター最高出力_ps_motor_highest_output = scrapy.Field() # モーター最高出力
    モーター最高トルク_nm_motor_maximum_torque = scrapy.Field() # モーター最高トルク
    モーター最高トルク_kgfm_motor_maximum_torque = scrapy.Field() # モーター最高トルク
    
    _200V充電時間_200v_charge_time = scrapy.Field() # 200V充電時間
    急速充電時間_fast_charge_time = scrapy.Field() # 急速充電時間
    最小回転半径_minimum_turning_radius = scrapy.Field() # 最小回転半径
    燃費_JC08モード_fuel_consumption_jc08_mode = scrapy.Field() # 燃費（JC08モード）
    燃費_10_15モード_fuel_consumption_10_15_mode = scrapy.Field() # 燃費（10.15モード）
    燃費基準達成率_fuel_efficiency_standard_achievement_rate = scrapy.Field() # 燃費基準達成率
    自動車税減税率_automobile_tax_reduction_rate = scrapy.Field() # 自動車税減税率
    自動車重量税減税率_automobile_weight_tax_reduction_rate = scrapy.Field() # 自動車重量税減税率
    取得税減税率_acquisition_tax_reduction_rate = scrapy.Field() # 取得税減税率
    自動車税_car_tax = scrapy.Field() # 自動車税
    自動車重量税_car_weight_tax = scrapy.Field() # 自動車重量税
    自動車取得税_car_acquisition_tax = scrapy.Field() # 自動車取得税
    全長_overall_length = scrapy.Field() # 全長
    全幅_overall_width = scrapy.Field() # 全幅
    全高_overall_height = scrapy.Field() # 全高
    ホイールベース_wheel_base = scrapy.Field() # ホイールベース
    最低地上高_未積載時_ground_clearance = scrapy.Field() # 最低地上高（未積載時）
    室内長_length_of_room = scrapy.Field() # 室内長
    室内高_room_height = scrapy.Field() # 室内高
    ヘッドルーム前_headroom_front = scrapy.Field() # ヘッドルーム前
    ヘッドルーム後_headroom_after = scrapy.Field() # ヘッドルーム後
    荷室容量_リアシート立_loading_capacity_rear_seat_standing = scrapy.Field() # 荷室容量（リアシート立）
    荷室容量_リアシート倒_loading_capacity_rear_seat_down = scrapy.Field() # 荷室容量（リアシート倒）
    荷室容量測定方式_loading_capacity_measurement_method = scrapy.Field() # 荷室容量測定方式
    リアシートまでの長さ_length_to_rear_seat = scrapy.Field() # リアシートまでの長さ
    タイヤサイズ_前_tire_size_before = scrapy.Field() # タイヤサイズ-前
    タイヤサイズ_後_after_tire_size = scrapy.Field() # タイヤサイズ-後
    ホイールサイズ_前_wheel_size_ago = scrapy.Field() # ホイールサイズ-前
    ホイールサイズ_後_wheel_size_after = scrapy.Field() # ホイールサイズ-後
    トレッド幅_前_tread_width_front = scrapy.Field() # トレッド幅-前
    トレッド幅_後_after_tread_width = scrapy.Field() # トレッド幅-後
    アルミホイール_aluminum_foil = scrapy.Field() # アルミホイール
    スペアタイヤ_spare_tire = scrapy.Field() # スペアタイヤ
    パンク修理キット_puncture_repair_kit = scrapy.Field() # パンク修理キット
    空気圧警告灯_air_pressure_warning_light = scrapy.Field() # 空気圧警告灯