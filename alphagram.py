import httpx
import asyncio
import logging, json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Alphagram:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}/"
        self.offset = None
        self.message_handlers = []
        self.callback_query_handler = []
        self.known_commands = set()
  
    def on_callback(self):
        def decorator(func):
            async def wrapper(callback):
            	await func(callback)
            self.callback_query_handler.append(wrapper)
            return wrapper
        return decorator  
        
    def on_message(self, commands=None):
        if commands:
            self.known_commands.update(commands)
        def decorator(handler_func):
            async def wrapper(message):
                if commands:                 
                    if "text" in message and any(message["text"].startswith(f"/{command}") for command in commands):
                        await handler_func(message)
                else:                    
                    if "text" in message and not any(message["text"].startswith(f"/{cmd}") for cmd in self.known_commands):
                        await handler_func(message)
            self.message_handlers.append(wrapper)
            return wrapper
        return decorator
        
    
    async def edit_message_text(self, chat_id, message_id, text, reply_markup=None):
    	url = f"{self.base_url}editMessageText"
    	data = {
    		"chat_id": chat_id,
    		"message_id": message_id,
    		"text": text,    	
    	}
    	if reply_markup is not None:
    		data["reply_markup"] = reply_markup
    	async with httpx.AsyncClient() as client:
            try:
            	response = await client.post(url, data=data)
            	response.raise_for_status()
            	return response.json()
            except:
            	try:
            		error_response = response.json()
            		error_message = error_response.get("description", "")
            		logging.error(error_message)
            	except Exception as e:
            		logging.error(e)    
    				
    async def send_message(self, chat_id, text, reply_markup=None, parse_mode=None):
        url = f"{self.base_url}sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
        }
        if reply_markup is not None:
        	data["reply_markup"] = reply_markup
        if parse_mode is not None:
        	data["parse_mode"] = parse_mode
        #if ReplyKeyboardRemove is not None:
#        	data["ReplyKeyboardRemove"] = {
#        	  "remove_keyboard": ReplyKeyboardRemove
#        	}
        async with httpx.AsyncClient() as client:
            try:
            	response = await client.post(url, data=data)
            	response.raise_for_status()
            	return response.json()
            except:
            	try:
            		error_response = response.json()
            		error_message = error_response.get("description", "")
            		logging.error(error_message)
            	except Exception as e:
            		logging.error(e)    

    async def send_photo(self, chat_id, photo, caption=None, reply_markup=None):
    	url = f"{self.base_url}sendPhoto"
    	data = {
    		"chat_id": chat_id,
    		"photo": photo,    		
    	}
    	if reply_markup is not None:
    		data["reply_markup"] = reply_markup
    	elif caption is not None:
    		data["caption"] = caption
    	async with httpx.AsyncClient() as client:
    		try:
	    	   response = await  client.post(url, data=data)
	    	   return response.json()
	    	except:
	    	  	 try:
	    	  	 	error_response = response.json()
	    	  	 	error_message = error_response.get("description", "")
	    	  	 	logging.error(error_message)
	    	  	 except Exception as e:
	    	  	        logging.error(e)
	    	  	        
    async def send_document(self, chat_id, document, caption=None, reply_markup=None):
    	url = f"{self.base_url}sendDocument"
    	data = {
    		"chat_id": chat_id,
    		"document": document,    		
    	}
    	if reply_markup is not None:
    		data["reply_markup"] = reply_markup
    	elif caption is not None:
    		data["caption"] = caption
    	async with httpx.AsyncClient() as client:
    		try:
	    	   response = await  client.post(url, data=data)
	    	   return response.json()
	    	except:
	    	  	 try:
	    	  	 	error_response = response.json()
	    	  	 	error_message = error_response.get("description", "")
	    	  	 	logging.error(error_message)
	    	  	 except Exception as e:
	    	  	        logging.error(e)
	    	  	        
    async def send_quiz(self, chat_id, question, correct_option_id, is_anonymous, type, options, explanation=None):
        url = f"{self.base_url}sendPoll"
        data = {
            "chat_id": int(chat_id),
            "question": question,
            "is_anonymous": True,
            "correct_option_id": correct_option_id,
            "type": type,
            "options": json.dumps(options)
        }
        if explanation is not None:
        	data['explanation'] = explanation
        async with httpx.AsyncClient() as client:
            try:
            	response = await client.post(url, data=data)
            	response.raise_for_status()
            	return response.json()
            except:
            	try:
            		error_response = response.json()
            		error_message = error_response.get("description", "")
            		logging.error(error_message)
            	except Exception as e:
            		logging.error(e)		       	
    
    async def delete_message(self, chat_id, message_id):
        url = f"{self.base_url}deleteMessage"
        data = {
            "chat_id": int(chat_id),
            "message_id": int(message_id),
        }
        async with httpx.AsyncClient() as client:
            try:
            	response = await client.post(url, data=data)
            	response.raise_for_status()
            	return response.json()
            except:
            	try:
            		error_response = response.json()
            		error_message = error_response.get("description", "")
            		logging.error(error_message)
            	except Exception as e:
            		logging.error(e)
            		
    async def send_video(self, chat_id, video, caption=None, reply_markup=None):
    	url = f"{self.base_url}sendVideo"
    	data = {
    		"chat_id": chat_id,
    		"video": video,    		
    	}
    	if reply_markup is not None:
    		data["reply_markup"] = reply_markup
    	elif caption is not None:
    		data["caption"] = caption
    	async with httpx.AsyncClient() as client:
    		try:
	    	   response = await  client.post(url, data=data)
	    	   return response.json()
	    	except:
	    	  	 try:
	    	  	 	error_response = response.json()
	    	  	 	error_message = error_response.get("description", "")
	    	  	 	logging.error(error_message)
	    	  	 except Exception as e:
	    	  	 	logging.error(e)
	    	  	 	
    async def get_updates(self):
        url = f"{self.base_url}getUpdates"
        params = {"offset": self.offset}
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()

    async def start(self):
        logging.info("Bot with polling started!")
        while True:
            try:
                updates = await self.get_updates()
                for update in updates.get("result", []):
                    self.offset = update["update_id"] + 1
                    if "message" in update:
                        message = update["message"]                      
                        for handler in self.message_handlers:
                            await handler(message)
                    if "callback_query" in update:
                        callback = update["callback_query"]
                        for handler in self.callback_query_handler:
                            await handler(callback)
            except Exception as e:
                logging.error(f"unable to connect: {e}")
                await asyncio.sleep(3)  
            await asyncio.sleep(1)  


class KeyboardButton:
    def __init__(self, text, request_contact=False, web_app_url=None):
        self.text = text
        self.web_app_url = web_app_url
        self.request_contact = request_contact

    def to_dict(self):
        data = {"text": self.text}
        if self.web_app_url:
        	data["web_app"] = {
        		"url": self.web_app_url
        	}
        elif self.request_contact:
        	data["request_contact"] = self.request_contact
        return data
        

class ReplyKeyboardMarkup:
    def __init__(self, resize_keyboard=True, row_width=1):
        self.resize_keyboard = resize_keyboard
        self.keyboard = []
        self.row_width = row_width
        self.current_row = -1
    
    def add_button(self, *buttons):
        for button in buttons:
            if self.current_row < 0 or len(self.keyboard[self.current_row]) >= self.row_width:
                self.keyboard.append([button.to_dict()])
                self.current_row += 1
            else:
                self.keyboard[self.current_row].append(button.to_dict())
                        
    def reply_to_json(self):
         return json.dumps({
	            "keyboard": self.keyboard,
	            "resize_keyboard": self.resize_keyboard
	        })


class InlineKeyboardButton:
    def __init__(self, text, callback_data=None, url=None, web_app_url=None):
        self.text = text
        self.callback_data = callback_data  
        self.url = url
        self.web_app_url = web_app_url
        
    def to_dict(self):
        data = {"text": self.text}
        if self.callback_data:
            data["callback_data"] = self.callback_data
        if self.url:
            data["url"] = self.url
        if self.web_app_url:
        	data["web_app"] = {
        		"url": self.web_app_url
        	}
        return data

class InlineKeyboardMarkup:
    def __init__(self, resize_keyboard=True, row_width=1):        
        self.keyboard = []
        self.row_width = row_width
        self.current_row = -1
        
    def add_button(self, *buttons):
        for button in buttons:
            if self.current_row < 0 or len(self.keyboard[self.current_row]) >= self.row_width:
                self.keyboard.append([button.to_dict()])
                self.current_row += 1
            else:
                self.keyboard[self.current_row].append(button.to_dict())

    def inline_to_json(self):
        data = json.dumps({
            "inline_keyboard": self.keyboard
        })        
        return data



 
