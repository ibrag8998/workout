import config_workout
import out_workout

from telebot import TeleBot, types
from time import sleep, time

bot = TeleBot(config_workout.token)

states = dict() # состояние юзверя ----------------------------------------------------------------

main_kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
main_kb.row('/teach', '/train')

ds_kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
ds_kb.row('Динамика', 'Статика')
ds_kb.row('⬅️Назад')

statics_kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
statics_kb.row('1', '2', '3', '4', '5')
statics_kb.row('6', '7', '8', '9', '10')
statics_kb.row('⬅️Назад')

dynamics_kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
dynamics_kb.row('1', '2', '3', '4', '5')
dynamics_kb.row('6', '7', '8', '9', '10')
dynamics_kb.row('⬅️Назад')

trains_kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
trains_kb.row('Икхван', 'Ганнибал')
trains_kb.row('⬅️Назад')

go_no_kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
go_no_kb.row('Начинаем', 'Не сейчас')

done_kb = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
done_kb.row('Сделано!', 'Не справляюсь!')
done_kb.row('Отмена тренировки')

# старт -------------------------------------------------------------------------------------------
@bot.message_handler(commands = ['start'])
def welcome(message):
	bot.send_message(message.chat.id, out_workout.welcome, reply_markup = main_kb)

# список команд -----------------------------------------------------------------------------------
@bot.message_handler(commands = ['help'])
def commands_list(message):
	bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

# тич ---------------------------------------------------------------------------------------------
@bot.message_handler(commands = ['teach'])
def teach_way_select(message):
	uid = message.from_user.id
	states[uid] = 'teach_select'
	bot.send_message(message.chat.id, 'Выбери направление:', reply_markup = ds_kb)

# тренировка --------------------------------------------------------------------------------------
@bot.message_handler(commands = ['train'])
def train_select(message):
	uid = message.from_user.id
	states[uid] = 'train'
	bot.send_message(message.chat.id, out_workout.train_select, reply_markup = trains_kb)


###################################################################################################


# ЛЯМБДЫ ------------------------------------------------------------------------------------------

# Выборка элемента --------------------------------------------------------------------------------
@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'teach_select')
def teach(message):
	uid = message.from_user.id
	if message.text == '⬅️Назад':
		bot.send_message(message.chat.id, 'Чем могу быть полезен?', reply_markup = main_kb)
	elif message.text == 'Динамика':
		bot.send_message(message.chat.id, out_workout.dynamics, reply_markup = dynamics_kb)
		states[uid] = 'teach_dynamics'
	elif message.text == 'Статика':
		bot.send_message(message.chat.id, out_workout.statics, reply_markup = statics_kb)
		states[uid] = 'teach_statics'
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

# трейн -------------------------------------------------------------------------------------------
@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'train')
def train(message):
	uid = message.from_user.id
	if message.text == '⬅️Назад':
		bot.send_message(message.chat.id, 'Чем могу быть полезен?', reply_markup = main_kb)
	elif message.text == 'Икхван':
		bot.send_message(message.chat.id, out_workout.ikhwan_train, reply_markup = go_no_kb)
		states[uid] = 'ikhwan_train'
	elif message.text == 'Ганнибал':
		bot.send_message(message.chat.id, out_workout.hannibal_train, reply_markup = go_no_kb)
		states[uid] = 'hannibal_train'
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)


###################################################################################################
########################################## ТУПО КОПИПАСТ ##########################################
###################################################################################################










# выкидыш обучалки --------------------------------------------------------------------------------
@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'teach_statics')
def teach_statics1(message):
	uid = message.from_user.id
	if message.text == '⬅️Назад':
		bot.send_message(message.chat.id, 'Чем могу быть полезен?', reply_markup = main_kb)
	elif message.text == '1':
		bot.send_message(message.chat.id, out_workout.t_skills['flag'][0], reply_markup = done_kb)
		states[uid] = 'flag_t_skills1'
	elif message.text == '2':
		bot.send_message(message.chat.id, out_workout.t_skills['dragon_flag'][0], reply_markup = done_kb)
		states[uid] = 'dragon_flag_t_skills1'
	elif message.text == '3':
		f = open('front_lever.jpg', 'rb')
		bot.send_photo(message.chat.id, f, reply_markup = done_kb)
		f.close()
		bot.send_message(message.chat.id, out_workout.t_skills['front_lever'][0], reply_markup = done_kb)
		states[uid] = 'front_lever_t_skills1'
	elif message.text == '4':
		f = open('back_lever.jpg', 'rb')
		bot.send_photo(message.chat.id, f, reply_markup = done_kb)
		f.close()
		bot.send_message(message.chat.id, out_workout.t_skills['back_lever'][0], reply_markup = done_kb)
		states[uid] = 'back_lever_t_skills1'
	elif message.text == '5':
		bot.send_message(message.chat.id, out_workout.t_skills['planche'][0], reply_markup = done_kb)
		states[uid] = 'planche_t_skills1'
	elif message.text == '6':
		bot.send_message(message.chat.id, out_workout.t_skills['maltese'][0], reply_markup = done_kb)
		states[uid] = 'maltese_t_skills1'
	elif message.text == '7':
		bot.send_message(message.chat.id, out_workout.t_skills['hefesto'][0], reply_markup = done_kb)
		states[uid] = 'hefesto_t_skills1'
	elif message.text == '8':
		bot.send_message(message.chat.id, out_workout.t_skills['angel'][0], reply_markup = done_kb)
		states[uid] = 'angel_t_skills1'
	elif message.text == '9':
		bot.send_message(message.chat.id, out_workout.t_skills['one_arm_pu'][0], reply_markup = done_kb)
		states[uid] = 'one_arm_pu_t_skills1'
	elif message.text == '10':
		bot.send_message(message.chat.id, out_workout.t_skills['handstand'][0], reply_markup = done_kb)
		states[uid] = 'handstand_t_skills1'
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states 
	and 't_skills1' in states[message.from_user.id])
def teach_statics2(message):
	uid = message.from_user.id
	chatid = message.chat.id
	if message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Поработай над базой и все получится', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	elif message.text == 'Сделано!':
		if states[uid] == 'flag_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['flag'][1], reply_markup = done_kb)
			states[uid] = 'flag_t_skills2'
		elif states[uid] == 'dragon_flag_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['dragon_flag'][1], reply_markup = done_kb)
			states[uid] = 'dragon_flag_t_skills2'
		elif states[uid] == 'front_lever_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['front_lever'][1], reply_markup = done_kb)
			states[uid] = 'front_lever_t_skills2'
		elif states[uid] == 'back_lever_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['back_lever'][1], reply_markup = done_kb)
			states[uid] = 'back_lever_t_skills2'
		elif states[uid] == 'planche_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['planche'][1], reply_markup = done_kb)
			states[uid] = 'planche_t_skills2'
		elif states[uid] == 'maltese_t_skills1':
			bot.send_message(chatid, 'Отлично!', reply_markup = main_kb)
		elif states[uid] == 'hefesto_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['hefesto'][1], reply_markup = done_kb)
			states[uid] = 'hefesto_t_skills2'
		elif states[uid] == 'angel_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['angel'][1], reply_markup = done_kb)
			states[uid] = 'angel_t_skills2'
		elif states[uid] == 'one_arm_pu_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['one_arm_pu'][1], reply_markup = done_kb)
			states[uid] = 'one_arm_pu_t_skills2'
		elif states[uid] == 'handstand_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['handstand'][1], reply_markup = done_kb)
			states[uid] = 'handstand_t_skills2'
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states 
	and 't_skills2' in states[message.from_user.id])
def teach_statics3(message):
	uid = message.from_user.id
	chatid = message.chat.id
	if message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Поработай над базой и все получится', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	elif message.text == 'Сделано!':
		if states[uid] == 'flag_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['flag'][2], reply_markup = done_kb)
			states[uid] = 'flag_t_skills3'
		elif states[uid] == 'dragon_flag_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['dragon_flag'][2], reply_markup = done_kb)
			states[uid] = 'dragon_flag_t_skills3'
		elif states[uid] == 'front_lever_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['front_lever'][2], reply_markup = done_kb)
			states[uid] = 'front_lever_t_skills3'
		elif states[uid] == 'back_lever_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['back_lever'][2], reply_markup = done_kb)
			states[uid] = 'back_lever_t_skills3'
		elif states[uid] == 'planche_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['planche'][2], reply_markup = done_kb)
			states[uid] = 'planche_t_skills3'
		elif states[uid] == 'hefesto_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['hefesto'][2], reply_markup = done_kb)
			states[uid] = 'hefesto_t_skills3'
		elif states[uid] == 'angel_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['angel'][2], reply_markup = done_kb)
			states[uid] = 'angel_t_skills3'
		elif states[uid] == 'one_arm_pu_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['one_arm_pu'][2], reply_markup = done_kb)
			states[uid] = 'one_arm_pu_t_skills3'
		elif states[uid] == 'handstand_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['handstand'][2], reply_markup = done_kb)
			states[uid] = 'handstand_t_skills3'
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states 
	and 't_skills3' in states[message.from_user.id])
def teach_statics4(message):
	uid = message.from_user.id
	chatid = message.chat.id
	if message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Поработай над базой и все получится', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	elif message.text == 'Сделано!':
		bot.send_message(chatid, 'Молодца', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

###################################################################################################

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'teach_dynamics')
def teach_dynamics1(message):
	uid = message.from_user.id
	if message.text == '⬅️Назад':
		bot.send_message(message.chat.id, 'Чем могу быть полезен?', reply_markup = done_kb)
	elif message.text == '1':
		bot.send_message(message.chat.id, out_workout.t_skills['sklepka'][0], reply_markup = done_kb)
		states[uid] = 'sklepka_t_skills1'
	elif message.text == '2':
		bot.send_message(message.chat.id, out_workout.t_skills['chair'][0], reply_markup = done_kb)
		states[uid] = 'chair_t_skills1'
	elif message.text == '3':
		bot.send_message(message.chat.id, out_workout.t_skills['under_bar'][0], reply_markup = done_kb)
		states[uid] = 'under_bar_t_skills1'
	elif message.text == '4':
		bot.send_message(message.chat.id, out_workout.t_skills['sun'][0], reply_markup = done_kb)
		states[uid] = 'sun_t_skills1'
	elif message.text == '5':
		bot.send_message(message.chat.id, out_workout.t_skills['ganger'][0], reply_markup = done_kb)
		states[uid] = 'ganger_t_skills1'
	elif message.text == '6':
		bot.send_message(message.chat.id, out_workout.t_skills['360'][0], reply_markup = done_kb)
		states[uid] = '360_t_skills1'
	elif message.text == '7':
		bot.send_message(message.chat.id, out_workout.t_skills['540'][0], reply_markup = done_kb)
		states[uid] = '540_t_skills1'
	elif message.text == '8':
		bot.send_message(message.chat.id, out_workout.t_skills['shrimpflip'][0], reply_markup = done_kb)
		states[uid] = 'shrimpflip_t_skills1'
	elif message.text == '9':
		bot.send_message(message.chat.id, out_workout.t_skills['korbut'][0], reply_markup = done_kb)
		states[uid] = 'korbut_t_skills1'
	elif message.text == '10':
		f = open('lach_gainer.mp4', 'rb')
		bot.send_video(message.chat.id, f, reply_markup = done_kb)
		f.close()
		bot.send_message(message.chat.id, out_workout.t_skills['lach_gainer'][0], reply_markup = done_kb)
		states[uid] = 'lach_gainer_t_skills1'
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states 
	and 't_skills1' in states[message.from_user.id])
def teach_dynamics2(message):
	uid = message.from_user.id
	chatid = message.chat.id
	if message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Поработай над базой и все получится', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	elif message.text == 'Сделано!':
		if states[uid] == 'sklepka_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['sklepka'][1], reply_markup = done_kb)
			states[uid] = 'sklepka_t_skills2'
		elif states[uid] == 'chair_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['chair'][1], reply_markup = done_kb)
			states[uid] = 'chair_t_skills2'
		elif states[uid] == 'under_bar_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['under_bar'][1], reply_markup = done_kb)
			states[uid] = 'under_bar_t_skills2'
		elif states[uid] == 'sun_t_skills1':
			bot.send_message(chatid, 'Отлично!', reply_markup = main_kb)
		elif states[uid] == 'ganger_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['ganger'][1], reply_markup = done_kb)
			states[uid] = 'ganger_t_skills2'
		elif states[uid] == '360_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['360'][1], reply_markup = done_kb)
			states[uid] = '360_t_skills2'
		elif states[uid] == '540_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['540'][1], reply_markup = done_kb)
			states[uid] = '540_t_skills2'
		elif states[uid] == 'korbut_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['korbut'][1], reply_markup = done_kb)
			states[uid] = 'korbut_t_skills2'
		elif states[uid] == 'lach_gainer_t_skills1':
			bot.send_message(chatid, out_workout.t_skills['lach_gainer'][1], reply_markup = done_kb)
			states[uid] = 'lach_gainer_t_skills2'
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states 
	and 't_skills2' in states[message.from_user.id])
def teach_dynamics3(message):
	uid = message.from_user.id
	chatid = message.chat.id
	if message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Поработай над базой и все получится', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	elif message.text == 'Сделано!':
		bot.send_message(chatid, '123456')
		if states[uid] == 'sklepka_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['sklepka'][2], reply_markup = done_kb)
			states[uid] = 'sklepka_t_skills3'
		elif states[uid] == 'chair_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['chair'][2], reply_markup = done_kb)
			states[uid] = 'chair_t_skills3'
		elif states[uid] == 'under_bar_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['under_bar'][2], reply_markup = done_kb)
			states[uid] = 'under_bar_t_skills3'
		elif states[uid] == 'ganger_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['ganger'][2], reply_markup = done_kb)
			states[uid] = 'ganger_t_skills3'
		elif states[uid] == '360_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['360'][2], reply_markup = done_kb)
			states[uid] = '360_t_skills3'
		elif states[uid] == '540_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['540'][2], reply_markup = done_kb)
			states[uid] = '540_t_skills3'
		elif states[uid] == 'korbut_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['korbut'][2], reply_markup = done_kb)
			states[uid] = 'korbut_t_skills3'
		elif states[uid] == 'lach_gainer_t_skills2':
			bot.send_message(chatid, out_workout.t_skills['lach_gainer'][2], reply_markup = done_kb)
			states[uid] = 'lach_gainer_t_skills3'
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states 
	and 't_skills3' in states[message.from_user.id])
def teach_dynamics4(message):
	uid = message.from_user.id
	chatid = message.chat.id
	if message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Поработай над базой и все получится', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	elif message.text == 'Сделано!':
		bot.send_message(chatid, 'Поздравляю!', reply_markup = done_kb)		
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)


###################################################################################################


# икхван ------------------------------------------------------------------------------------------
@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train')
def ikhwan_train1(message):
	uid = message.from_user.id
	if message.text == 'Начинаем':
		bot.send_message(message.chat.id, 'Итак, 20 алмазных отжиманий!', reply_markup = done_kb)
		states[uid] = 'ikhwan_train1'
	elif message.text == 'Не сейчас':
		bot.send_message(message.chat.id, 'Жаль...', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train1')
def ikhwan_train2(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '20 отжиманий с руками у пояса!', reply_markup = done_kb)
		states[uid] = 'ikhwan_train2'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Пробуй пока что-то полегче', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train2')
def ikhwan_train3(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '60 сек лягушка! Погнали!', reply_markup = done_kb)
		states[uid] = 'ikhwan_train3'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Пробуй пока что-то полегче', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train3')
def ikhwan_train4(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '20 отжиманий с руками у пояса!', reply_markup = done_kb)
		states[uid] = 'ikhwan_train4'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Учи лягушку, развивает баланс', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train4')
def ikhwan_train5(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '15 суперменов', reply_markup = done_kb)
		states[uid] = 'ikhwan_train5'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Попробуй пока что-то полегче', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train5')
def ikhwan_train6(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '15 отжиманий в стойке у стены', reply_markup = done_kb)
		states[uid] = 'ikhwan_train6'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Понимаю, это трудно. Подкачайся 💪 :D', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train6')
def ikhwan_train7(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '15 хинду отжиманий', reply_markup = done_kb)
		states[uid] = 'ikhwan_train7'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Тренируй плечи и все будет ОК 💪', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train7')
def ikhwan_train8(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '15 армейских отжиманий', reply_markup = done_kb)
		states[uid] = 'ikhwan_train8'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Жаль... Ты почти дошел до финиша 😢', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train8')
def ikhwan_train9(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '60 сек планка! Погнали!', reply_markup = done_kb)
		states[uid] = 'ikhwan_train9'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Улучши плечи и пробуй еще раз 💪', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train9')
def ikhwan_train10(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отдохни полторы минутки')
		sleep(90)
		bot.send_message(message.chat.id, '30 отжиманий на стойках', reply_markup = done_kb)
		states[uid] = 'ikhwan_train10'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Почти дошел до финиша, эх 😢', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'ikhwan_train10')
def ikhwan_train11(message):
	uid = message.from_user.id
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отлично! 💪💪', reply_markup = main_kb)
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Это было последнее упражнение... 😢', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)


###################################################################################################


# ганнибал ----------------------------------------------------------------------------------------
@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'hannibal_train')
def hannibal_train1(message):
	uid = message.from_user.id
	if message.text == 'Начинаем':
		bot.send_message(message.chat.id, 'Отжимания! Погнали! Отдых между подходами на твой выбор')
		bot.send_message(message.chat.id, '30/29/28/27/26/25/24/23/22/21', reply_markup = done_kb)
		states[uid] = 'hannibal_train1'
	elif message.text == 'Не сейчас':
		bot.send_message(message.chat.id, 'Жаль...', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'hannibal_train1')
def hannibal_train2(message):
	uid = message.from_user.id
	sleep(0.5)
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Подтягивания прямым хватом! Не торопись, следи за качеством!')
		bot.send_message(message.chat.id, '10/9/8/7/6/5/5/5/5/5', reply_markup = done_kb)
		states[uid] = 'hannibal_train2'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Потренируйся еще, попробуй позже', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'hannibal_train2')
def hannibal_train3(message):
	uid = message.from_user.id
	sleep(0.5)
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отжимания на брусьях! Следя за качеством, не думай о времени!')
		bot.send_message(message.chat.id, '20/19/18/17/16/15/14/13/12/11', reply_markup = done_kb)
		states[uid] = 'hannibal_train3'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Тренируйся больше, все получится', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'hannibal_train3')
def hannibal_train4(message):
	uid = message.from_user.id
	sleep(0.5)
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Подтягивания обратным хватом! Это последнее! 💪')
		bot.send_message(message.chat.id, '10/9/8/7/6/5/5/5/5/5', reply_markup = done_kb)
		states[uid] = 'hannibal_train4'
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Нужно подкачать трицепс', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

@bot.message_handler(func = lambda message: message.from_user.id in states
	and states[message.from_user.id] == 'hannibal_train4')
def hannibal_train5(message):
	sleep(0.5)
	if message.text == 'Сделано!':
		bot.send_message(message.chat.id, 'Отлично! 💪', reply_markup = main_kb)
	elif message.text == 'Не справляюсь!':
		bot.send_message(message.chat.id, 'Эхх, это было последнее упражнение 😢', reply_markup = main_kb)
	elif message.text == 'Отмена тренировки':
		bot.send_message(message.chat.id, 'Надеюсь, у тебя уважительная причина', reply_markup = main_kb)
	else:
		bot.send_message(message.chat.id, out_workout.supported_commands, reply_markup = main_kb)

if __name__ == '__main__':
	bot.polling()