import scrapy
import re

from scrapy.spiders import CrawlSpider, Rule 
from scrapy.linkextractors import LinkExtractor
from parking_min.items import Headline 

class ParkingMinClawlSpider(CrawlSpider):
    name = 'parking_min_clawl'
    allowed_domains = ['kakaku.com']
    start_urls = ['https://kakaku.com/item/K0000368745/']
    
    custom_settings = {
    # CSVファイルに出力する順番を設定
    'FEED_EXPORT_FIELDS': [
        "url",
        "生産国_country",
        "メーカー_maker",
        "ジャンル_genre",
        "モデル名_model_name",
        "グレード名_model_grade",
        "新車価格_new_car_price",
        "発売日_release_date",
        "発売区分_release_category",
        "新車販売状況_new_car_sales_situation",
        "型式_model_number",
        "動力分類_power_classification",
        "駆動方式_drive_system",
        "ハンドル位置_handle_position",
        "乗車定員_boarding_capacity",
        "ドア数_number_of_doors",
        "シート列数_number_of_sheet_columns",
        "車両重量_vehicle_weight",
        "車両総重量_vehicle_gross_weight",
        "排気量_displacement",
        "最高出力_kw_highest_output",
        "最高出力_ps_highest_output",
        "最高トルク_nm_maximum_torque",
        "最高トルク_kgfm_maximum_torque",
        "過給機_turbocharger",
        "アイドリングストップ_idling_stop",
        "燃料_fuel",
        "燃料タンク容量_fuel_tank_capacity",
        "総電力量_total_power",
        "充電走行距離_charging_distance",
        "モーター最高出力_kw_motor_highest_output",
        "モーター最高出力_ps_motor_highest_output",
        "モーター最高トルク_nm_motor_maximum_torque",
        "モーター最高トルク_kgfm_motor_maximum_torque",
        "_200V充電時間_200v_charge_time",
        "急速充電時間_fast_charge_time",
        "最小回転半径_minimum_turning_radius",
        "燃費_JC08モード_fuel_consumption_jc08_mode",
        "燃費_10_15モード_fuel_consumption_10_15_mode",
        "燃費基準達成率_fuel_efficiency_standard_achievement_rate",
        "自動車税減税率_automobile_tax_reduction_rate",
        "自動車重量税減税率_automobile_weight_tax_reduction_rate",
        "取得税減税率_acquisition_tax_reduction_rate",
        "自動車税_car_tax","自動車重量税_car_weight_tax",
        "自動車取得税_car_acquisition_tax",
        "全長_overall_length",
        "全幅_overall_width",
        "全高_overall_height",
        "ホイールベース_wheel_base",
        "最低地上高_未積載時_ground_clearance",
        "室内長_length_of_room","室内高_room_height",
        "ヘッドルーム前_headroom_front",
        "ヘッドルーム後_headroom_after",
        "荷室容量_リアシート立_loading_capacity_rear_seat_standing",
        "荷室容量_リアシート倒_loading_capacity_rear_seat_down",
        "荷室容量測定方式_loading_capacity_measurement_method",
        "リアシートまでの長さ_length_to_rear_seat",
        "タイヤサイズ_前_tire_size_before",
        "タイヤサイズ_後_after_tire_size",
        "ホイールサイズ_前_wheel_size_ago",
        "ホイールサイズ_後_wheel_size_after",
        "トレッド幅_前_tread_width_front",
        "トレッド幅_後_after_tread_width",
        "アルミホイール_aluminum_foil",
        "スペアタイヤ_spare_tire",
        "パンク修理キット_puncture_repair_kit",
        "空気圧警告灯_air_pressure_warning_light"],
    }

    #リンクをたどるためのルールのリスト。
    rules = (
        # Rule(LinkExtractor(allow=r'/maker/[a-zA-Z0-9-]+/$'), ),
        # Rule(LinkExtractor(allow=r'/maker/[a-zA-Z0-9-]+/all/$'), ),
        # Rule(LinkExtractor(allow=r'/item/[a-zA-Z0-9]+/$'), ),
        Rule(LinkExtractor(allow=r'/item/[a-zA-Z0-9]+/catalog/$'),) ,
        #Rule(LinkExtractor(allow=r'/item/[a-zA-Z0-9]+/catalog/$'), callback='parse_model',follow=True)  #ここで「モデル名＋年代」「価格」「ジャンル」「人気ランキング」を取得
        Rule(LinkExtractor(allow=r'/item/[a-zA-Z0-9]+/catalog/[a-zA-Z0-9=]+/$'), callback = 'parse_topics')
    )
    
    
    def parse_topics(self, response):
        
    
        maker = response.css('.p-main_type-maker::text').extract_first() #生産国を取得するため
        
        genre = '.p-main_type-bodytype::text'
        model_name = 'li.l-h_bread_drops:nth-last-child(2) span a span::text'
        model_grade = 'li.l-h_bread_drops:nth-last-child(1) span strong::text'
        new_car_price = '#specDetail table.specSheet tbody tr th:contains("新車価格")+td::text'
        release_date = '#specDetail table.specSheet tbody tr th:contains("発売日")+td::text'
        release_category = '#specDetail table.specSheet tbody tr th:contains("発売区分")+td::text'
        new_car_sales_situation = '#specDetail table.specSheet tbody tr th:contains("新車販売状況")+td::text'
        model_number = '#specDetail table.specSheet tbody tr th:contains("型式")+td::text'
        power_classification = '#specDetail table.specSheet tbody tr th:contains("動力分類")+td::text'
        drive_system = '#specDetail table.specSheet tbody tr th:contains("駆動方式")+td::text' #ここでハイブリットか稲香
        handle_position = '#specDetail table.specSheet tbody tr th:contains("ハンドル位置")+td::text'
        boarding_capacity = '#specDetail table.specSheet tbody tr th:contains("乗車定員")+td::text'
        number_of_doors = '#specDetail table.specSheet tbody tr th:contains("ドア数")+td::text'
        number_of_sheet_columns = '#specDetail table.specSheet tbody tr th:contains("シート列数")+td::text'
        vehicle_weight = '#specDetail table.specSheet tbody tr th:contains("車両重量")+td::text'
        vehicle_gross_weight = '#specDetail table.specSheet tbody tr th:contains("車両総重量")+td::text'
        displacement = '#specDetail table.specSheet tbody tr th:contains("排気量")+td::text'
        
        #highest_output = '#specDetail table.specSheet tbody tr th:contains("(kW[PS]/rpm)")+td::text'
        highest_output = response.css('#specDetail table.specSheet tbody tr th:contains("(kW[PS]/rpm)")+td::text').extract_first() #分割処理を行う
        highest_output_array = re.split('[\[\]/]', highest_output)
        
        #maximum_torque = '#specDetail table.specSheet tbody tr th:contains("(N・m[kgf・m]/rpm)")+td::text'
        maximum_torque = response.css('#specDetail table.specSheet tbody tr th:contains("(N・m[kgf・m]/rpm)")+td::text').extract_first() #分割処理を行う
        maximum_torque_array = re.split('[\[\]/]', maximum_torque)
        
        turbocharger = '#specDetail table.specSheet tbody tr th:contains("過給機")+td::text'
        idling_stop = '#specDetail table.specSheet tbody tr th:contains("アイドリングストップ")+td::text'
        fuel = '#specDetail .specSheetBox:nth-child(2)  table tbody tr:nth-child(7) td::text'
        fuel_tank_capacity = '#specDetail table.specSheet:nth-child(2) tbody tr th:contains("燃料タンク容量")+td::text'
        total_power = '#specDetail table.specSheet tbody tr th:contains("総電力量")+td::text'
        charging_distance = '#specDetail table.specSheet tbody tr th:contains("充電走行距離")+td::text'
        
        # motor_highest_output = '#specDetail table.specSheet tbody tr th:contains("(kW[PS])")+td::text'
        motor_highest_output = response.css('#specDetail table.specSheet tbody tr th:contains("(kW[PS])")+td::text').extract_first() #分割処理を行う
        motor_highest_output_array = re.split('[\[\]/]', motor_highest_output)
        
        # motor_maximum_torque = '#specDetail table.specSheet tbody tr th:contains("(N・m[kgf・m])")+td::text'
        motor_maximum_torque = response.css('#specDetail table.specSheet tbody tr th:contains("(N・m[kgf・m])")+td::text').extract_first() #分割処理を行う
        motor_maximum_torque_array = re.split('[\[\]/]', motor_maximum_torque)
        
        _200v_charge_time = '#specDetail table.specSheet tbody tr th:contains("200V充電時間")+td::text'
        fast_charge_time = '#specDetail table.specSheet tbody tr th:contains("急速充電時間")+td::text'
        minimum_turning_radius = '#specDetail table.specSheet tbody tr th:contains("最小回転半径")+td::text'
        fuel_consumption_jc08_mode = '#specDetail table.specSheet tbody tr th:contains("燃費（JC08モード）")+td::text'
        fuel_consumption_10_15_mode = '#specDetail table.specSheet tbody tr th:contains("燃費（10.15モード）")+td::text'
        fuel_efficiency_standard_achievement_rate = '#specDetail table.specSheet tbody tr th:contains("燃費基準達成率")+td::text'
        automobile_tax_reduction_rate = '#specDetail table.specSheet tbody tr th:contains("自動車税減税率")+td::text'
        automobile_weight_tax_reduction_rate = '#specDetail table.specSheet tbody tr th:contains("自動車重量税減税率")+td::text'
        acquisition_tax_reduction_rate = '#specDetail table.specSheet tbody tr th:contains("取得税減税率")+td::text'
        car_tax = '#specDetail .specSheetBox:nth-child(9) table tbody tr:nth-child(2) td::text'
        car_weight_tax = '#specDetail .specSheetBox:nth-child(9) table tbody tr:nth-child(3) td::text'
        car_acquisition_tax = '#specDetail table.specSheet tbody tr th:contains("自動車取得税")+td::text'
        overall_length = '#specDetail table.specSheet tbody tr th:contains("全長")+td::text'
        overall_width = '#specDetail table.specSheet tbody tr th:contains("全幅")+td::text'
        overall_height = '#specDetail table.specSheet tbody tr th:contains("全高")+td::text'
        wheel_base = '#specDetail table.specSheet tbody tr th:contains("ホイールベース")+td::text'
        ground_clearance = '#specDetail table.specSheet tbody tr th:contains("最低地上高（未積載時）")+td::text'
        length_of_room = '#specDetail table.specSheet tbody tr th:contains("室内長")+td::text'
        room_height = '#specDetail table.specSheet tbody tr th:contains("室内高")+td::text'
        headroom_front = '#specDetail table.specSheet tbody tr th:contains("ヘッドルーム 前")+td::text'
        headroom_after = '#specDetail table.specSheet tbody tr th:contains("ヘッドルーム 後")+td::text'
        loading_capacity_rear_seat_standing = '#specDetail table.specSheet tbody tr th:contains("リアシート立")+td::text'
        loading_capacity_rear_seat_down = '#specDetail table.specSheet tbody tr th:contains("リアシート倒")+td::text'
        loading_capacity_measurement_method = '#specDetail table.specSheet tbody tr th:contains("測定方式")+td::text'
        length_to_rear_seat = '#specDetail table.specSheet tbody tr th:contains("リアシートまでの長さ")+td::text'
        tire_size_before = '#specDetail table.specSheet tbody tr th:contains("タイヤサイズ 前")+td::text'
        after_tire_size = '#specDetail table.specSheet tbody tr th:contains("タイヤサイズ 後")+td::text'
        wheel_size_ago = '#specDetail table.specSheet tbody tr th:contains("ホイールサイズ 前")+td::text'
        wheel_size_after = '#specDetail table.specSheet tbody tr th:contains("ホイールサイズ 後")+td::text'
        tread_width_front = '#specDetail table.specSheet tbody tr th:contains("トレッド幅 前")+td::text'
        after_tread_width = '#specDetail table.specSheet tbody tr th:contains("トレッド幅 後")+td::text'
        aluminum_foil = '#specDetail table.specSheet tbody tr th:contains("アルミホイール")+td::text'
        spare_tire = '#specDetail table.specSheet tbody tr th:contains("スペアタイヤ")+td::text'
        puncture_repair_kit = '#specDetail table.specSheet tbody tr th:contains("パンク修理キット")+td::text'
        air_pressure_warning_light = '#specDetail table.specSheet tbody tr th:contains("空気圧警告灯")+td::text'
        
        
        jp = ['トヨタ', '日産', 'ホンダ', 'マツダ', 'スズキ', 'ダイハツ', '三菱', 'スバル', 'レクサス', '光岡', 'いすゞ', 'GLM']
        gr = ['フォルクスワーゲン', 'BMW', 'YES！', 'アウディ', 'アルピナ', 'オペル', 'スマート', 'ポルシェ', 'マイバッハ', 'メルセデス・ベンツ', 'メルセデスAMG', 'メルセデス・マイバッハ']
        us = ['キャデラック', 'クライスラー', 'サリーン', 'ジープ', 'シボレー', 'ダッジ', 'テスラ', 'ハマー', 'フォード', 'マーキュリー', 'リンカーン']
        gb = ['AC', 'MG', 'TVR', 'アストンマーチン', 'ケーターハム', 'ジャガー', 'デイムラー', 'ノーブル', 'ベントレー', 'マクラーレン', 'ミニ', 'モーガン', 'ランドローバー', 'ローバー', 'ロータス', 'ロールス・ロイス']
        it = ['アルファロメオ', 'フィアット', 'フェラーリ', 'マセラティ', 'ランチア', 'ランボルギーニ']
        fr = ['シトロエン', 'ブガッティ', 'プジョー', 'ルノー', 'アルピーヌ']
        se = ['サーブ', 'ボルボ']
        nl = ['ドンカーブート']
        kr = ['ヒュンダイ']
        za = ['バーキン']
        my = ['プロトン']
        
        
        def country_judge(i):
            if i in jp:
                country = '日本'
            elif i in gr:
                country = 'ドイツ'
            elif i in us:
                country = 'アメリカ'
            elif i in gb:
                country = 'イギリス'
            elif i in it:
                country = 'イタリア'
            elif i in fr:
                country = 'フランス'
            elif i in se:
                country = 'スウェーデン'
            elif i in nl:
                country = 'オランダ'
            elif i in kr:
                country = '韓国'
            elif i in za:
                country = '南アフリカ'
            elif i in my:
                country = 'マレーシア'
            else:
                country = '不明'
            return country
        country = country_judge(maker)
        
        
   
        
        #item.pyに値を送信
        item = Headline()  # Headlineオブジェクトを作成。
        item['url'] = response.url
        item['生産国_country'] = country
        item['メーカー_maker'] = maker
        item['ジャンル_genre'] = response.css(genre).extract_first()
        item['モデル名_model_name'] = response.css(model_name).extract_first()
        item['グレード名_model_grade'] = response.css(model_grade).extract_first()
        item['新車価格_new_car_price'] = response.css(new_car_price).extract_first()
        item['発売日_release_date'] = response.css(release_date).extract_first()
        item['発売区分_release_category'] = response.css(release_category).extract_first()
        item['新車販売状況_new_car_sales_situation'] = response.css(new_car_sales_situation).extract_first()
        item['型式_model_number'] = response.css(model_number).extract_first()
        item['動力分類_power_classification'] = response.css(power_classification).extract_first()
        item['駆動方式_drive_system'] = response.css(drive_system).extract_first()
        item['ハンドル位置_handle_position'] = response.css(handle_position).extract_first()
        item['乗車定員_boarding_capacity'] = response.css(boarding_capacity).extract_first()
        item['ドア数_number_of_doors'] = response.css(number_of_doors).extract_first()
        item['シート列数_number_of_sheet_columns'] = response.css(number_of_sheet_columns).extract_first()
        item['車両重量_vehicle_weight'] = response.css(vehicle_weight).extract_first()
        item['車両総重量_vehicle_gross_weight'] = response.css(vehicle_gross_weight).extract_first()
        item['排気量_displacement'] = response.css(displacement).extract_first()
        
        item['最高出力_kw_highest_output'] = highest_output_array[0]
        item['最高出力_ps_highest_output'] = highest_output_array[1]
        
        item['最高トルク_nm_maximum_torque'] = maximum_torque_array[0]
        item['最高トルク_kgfm_maximum_torque'] = maximum_torque_array[1]
        
        item['過給機_turbocharger'] = response.css(turbocharger).extract_first()
        item['アイドリングストップ_idling_stop'] = response.css(idling_stop).extract_first()
        item['燃料_fuel'] = response.css(fuel).extract_first()
        item['燃料タンク容量_fuel_tank_capacity'] = response.css(fuel_tank_capacity).extract_first()
        item['総電力量_total_power'] = response.css(total_power).extract_first()
        item['充電走行距離_charging_distance'] = response.css(charging_distance).extract_first()
        
        item['モーター最高出力_kw_motor_highest_output'] = motor_highest_output_array[0]
        item['モーター最高出力_ps_motor_highest_output'] = motor_highest_output_array[1]
        
        item['モーター最高トルク_nm_motor_maximum_torque'] = motor_maximum_torque_array[0]
        item['モーター最高トルク_kgfm_motor_maximum_torque'] = motor_maximum_torque_array[1]
        
        item['_200V充電時間_200v_charge_time'] = response.css(_200v_charge_time).extract_first()
        item['急速充電時間_fast_charge_time'] = response.css(fast_charge_time).extract_first()
        item['最小回転半径_minimum_turning_radius'] = response.css(minimum_turning_radius).extract_first()
        item['燃費_JC08モード_fuel_consumption_jc08_mode'] = response.css(fuel_consumption_jc08_mode).extract_first()
        item['燃費_10_15モード_fuel_consumption_10_15_mode'] = response.css(fuel_consumption_10_15_mode).extract_first()
        item['燃費基準達成率_fuel_efficiency_standard_achievement_rate'] = response.css(fuel_efficiency_standard_achievement_rate).extract_first()
        item['自動車税減税率_automobile_tax_reduction_rate'] = response.css(automobile_tax_reduction_rate).extract_first()
        item['自動車重量税減税率_automobile_weight_tax_reduction_rate'] = response.css(automobile_weight_tax_reduction_rate).extract_first()
        item['取得税減税率_acquisition_tax_reduction_rate'] = response.css(acquisition_tax_reduction_rate).extract_first()
        item['自動車税_car_tax'] = response.css(car_tax).extract_first()
        item['自動車重量税_car_weight_tax'] = response.css(car_weight_tax).extract_first()
        item['自動車取得税_car_acquisition_tax'] = response.css(car_acquisition_tax).extract_first()
        item['全長_overall_length'] = response.css(overall_length).extract_first()
        item['全幅_overall_width'] = response.css(overall_width).extract_first()
        item['全高_overall_height'] = response.css(overall_height).extract_first()
        item['ホイールベース_wheel_base'] = response.css(wheel_base).extract_first()
        item['最低地上高_未積載時_ground_clearance'] = response.css(ground_clearance).extract_first()
        item['室内長_length_of_room'] = response.css(length_of_room).extract_first()
        item['室内高_room_height'] = response.css(room_height).extract_first()
        item['ヘッドルーム前_headroom_front'] = response.css(headroom_front).extract_first()
        item['ヘッドルーム後_headroom_after'] = response.css(headroom_after).extract_first()
        item['荷室容量_リアシート立_loading_capacity_rear_seat_standing'] = response.css(loading_capacity_rear_seat_standing).extract_first()
        item['荷室容量_リアシート倒_loading_capacity_rear_seat_down'] = response.css(loading_capacity_rear_seat_down).extract_first()
        item['荷室容量測定方式_loading_capacity_measurement_method'] = response.css(loading_capacity_measurement_method).extract_first()
        item['リアシートまでの長さ_length_to_rear_seat'] = response.css(length_to_rear_seat).extract_first()
        item['タイヤサイズ_前_tire_size_before'] = response.css(tire_size_before).extract_first()
        item['タイヤサイズ_後_after_tire_size'] = response.css(after_tire_size).extract_first()
        item['ホイールサイズ_前_wheel_size_ago'] = response.css(wheel_size_ago).extract_first()
        item['ホイールサイズ_後_wheel_size_after'] = response.css(wheel_size_after).extract_first()
        item['トレッド幅_前_tread_width_front'] = response.css(tread_width_front).extract_first()
        item['トレッド幅_後_after_tread_width'] = response.css(after_tread_width).extract_first()
        item['アルミホイール_aluminum_foil'] = response.css(aluminum_foil).extract_first()
        item['スペアタイヤ_spare_tire'] = response.css(spare_tire).extract_first()
        item['パンク修理キット_puncture_repair_kit'] = response.css(puncture_repair_kit).extract_first()
        item['空気圧警告灯_air_pressure_warning_light'] = response.css(air_pressure_warning_light).extract_first()
        
        yield item  # Itemをyieldして、データを抽出する。
                
